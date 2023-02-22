import logging



# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a', format='%(asctime)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def add_few_number(a: int, b: int, c: int) -> int:
    logging.debug(f'Received numbers: a {a} and b:{b} and c:{c}')
    try:
        return int(a) + int(b) + int(c)
    except Exception as e:
        logging.warning(f'Entered number is a string a-> {a}  and b-> {b} and c-> {c} Error msg: {e}')
    

a, b, c = input("Enter three numbers with space between them: ").split()


add_few_number(a, b, c)
