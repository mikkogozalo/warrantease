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
    void create(account_name username) {
        require_auth(username);
        print(name{username});
    }
private:
    /// @abi struct warranties
    struct warranty {
        account_name account;
        account_name manufacturer;
        string serial_number;
        uint64_t date_of_purchase;
        uint64_t length_of_warranty;

        string primary_key() const { return serial_number; }
        account_name by_account() const { return account; }
    };

    /// @abi table
    typedef eosio::multi_index<
            N(warranties),
            warranty,
            indexed_by<N(byaccount), const_mem_fun<warranty, uint64_t, &warranty::by_account>>
            > warranties;

    warranties _warranties;
};

EOSIO_ABI( warrantease, (create) )