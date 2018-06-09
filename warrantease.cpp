#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>
using namespace eosio;
using std::string;

class warrantease : public eosio::contract {
public:
    warrantease(account_name a):
        contract(a),
        _warranties(a, a)
    {}

    /// @abi action
    void create(account_name username,
                account_name manufacturer,
                uint64_t serial_number,
                uint64_t length_of_warranty,
                string coverage,
                string region,
                string contact_details,
                string remarks) {
        require_auth(manufacturer);
        uint64_t date_of_purchase = now();
        _warranties.emplace(get_self(), [&]( auto& p ) {
            p.account = username;
            p.manufacturer = manufacturer;
            p.serial_number = serial_number;
            p.length_of_warranty = length_of_warranty;
            p.date_of_purchase = date_of_purchase;
            p.coverage = coverage;
            p.region = region;
            p.contact_details = contact_details;
            p.remarks = remarks + remarks == "" ? : "" : "\n";
        });
    }

    /// @abi action
    void changenickname(account_name owner, uint64_t serial_number, string nickname) {
        require_auth(owner);
        auto itr = _warranties.find(serial_number);
        eosio_assert(itr != _warranties.end(), "Product not in database");
        _warranties.modify(itr, get_self(), [&](auto& p ) {
            p.nickname = nickname;
        });
    }

    /// @abi action
    void addremark(account_name manufacturer, uint64_t serial_number, string remark) {
        require_auth(manufacturer);
        auto itr = _warranties.find(serial_number);
        eosio_assert(itr != _warranties.end(), "Product not in database");
        _warranties.modify(itr, get_self(), [&](auto& p ) {
            p.remarks = p.remarks + remark + "\n";
        });
    }

    /// @abi action
    void transfer(account_name old_account, account_name new_account, uint64_t serial_number) {
        require_auth(old_account);
        // TODO: Check if old account == new_account
        auto itr = _warranties.find(serial_number);
        eosio_assert(itr != _warranties.end(), "Product not in database");
        _warranties.modify(itr, get_self(), [&](auto& p ) {
            p.account = new_account
        });
    }

    /// @abi action
    void isvalid(uint64_t
                 serial_number) {
        auto itr = _warranties.find(serial_number);
        eosio_assert(itr != _warranties.end(), "Product not in database");
        if((itr->date_of_purchase + 86400 * itr -> length_of_warranty) > now()) {
            print("We are covered");
        } else {
            print("We are not covered");
        }
    }

private:
    /// @abi table warranties i64
    struct warranty {
        account_name account;               // DONE
        account_name manufacturer;          // DONE
        uint64_t serial_number;             // DONE
        uint64_t date_of_purchase;          // computed field
        uint64_t length_of_warranty;        // Done

        bool is_void;                       //

        string coverage;                    //
        string region;                      //
        string contact_details;             //
        string nickname;                    //
        string remarks;                     //

        uint64_t primary_key() const { return serial_number; }
        account_name by_account() const { return account; }
        account_name by_manufacturer() const { return manufacturer; }
    };

    /// @abi table
    typedef eosio::multi_index<
            N(warranties),
            warranty,
            indexed_by<N(byaccount), const_mem_fun<warranty, account_name , &warranty::by_account>>,
            indexed_by<N(bymanufacturer), const_mem_fun<warranty, account_name, &warranty::by_manufacturer>>
            > warranties;

    warranties _warranties;
};

EOSIO_ABI( warrantease, (create)(isvalid)(addremark)(transfer)(changenickname) )