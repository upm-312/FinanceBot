from get_names import get_names
from find_figi import find_FIGI
from get_history import get_history
from token_1 import TOKEN
from to_decimal import process_quotation_data

def main():
    
    get_names(TOKEN)
    get_history(find_FIGI())
    
    process_quotation_data()

if __name__ == "__main__":
    main()