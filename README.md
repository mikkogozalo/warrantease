# WarrantEase
*Easy, secure product warranty registration and claims*

## Smart Contract (`warrantease`)

### Actions

**create** - Create a warranty record

    void create(account_name username,
                account_name manufacturer,
                uint64_t serial_number,
                uint64_t length_of_warranty,
                string coverage,
                string region,
                string contact_details,
                string remarks);
                
**changenick** - Change the nickname of the item

    void changenick(account_name account, uint64_t serial_number, string nickname)
    
**addremark** - Appends remark to the warranty remarks, keeping track of old remarks

    void addremark(account_name manufacturer, uint64_t serial_number, string remark)
    
**transfer** - Transfer the ownership of an item to another user account

    void transfer(account_name old_account, account_name new_account, uint64_t serial_number)
    
**isvalid** - Check the validity of the warranty

    void isvalid(uint64_t serial_number)

**validate** - Manufacturer revalidates a warranty
 
    void validate(account_name manufacturer,
                    uint64_t serial_number)
       
**invalidate** - Manufacturer invalidates a warranty
 
    void invalidate(account_name manufacturer,
                    uint64_t serial_number);

**list** - List all warranties associated with an account
 
        void list(account_name account);

**extend** - Extend a warranty's validity duration
 
    void extend(account_name manufacturer,
                    uint64_t serial_number, int64_t days)


