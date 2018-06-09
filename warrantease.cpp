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
    void create(account_name username, account_name manufacturer, uint64_t serial_number, uint64_t length_of_warranty) {
        require_auth(manufacturer);
        uint64_t date_of_purchase = now();
        _warranties.emplace(get_self(), [&]( auto& p ) {
            p.account = username;
            p.manufacturer = manufacturer;
            p.serial_number = serial_number;
            p.length_of_warranty = length_of_warranty;
            p.date_of_purchase = date_of_purchase;
        });
    }

    void dummy(uint64_t) {

    }

    void isvalid(uint64_t serial_number) {
        auto itr = _warranties.find(serial_number);
        eosio_assert(itr != _warranties.end(), "Product not in database");
        print(itr->date_of_purchase + 86400 * itr -> length_of_warranty);
        print(now());
        if((itr->date_of_purchase + 86400 * itr -> length_of_warranty) <= now()) {
            print("We are covered");
        } else {
            print("We are not covered");
        }
    }

private:
    /// @abi table warranties i64
    struct warranty {
        account_name account;
        account_name manufacturer;
        uint64_t serial_number;
        uint64_t date_of_purchase;
        uint64_t length_of_warranty;
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

EOSIO_ABI( warrantease, (create)(isvalid)(dummy) )