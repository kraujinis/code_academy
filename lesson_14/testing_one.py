import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def add_few_number(a: int, b: int) -> int:
    logging.debug(f'Received numbers: a {a} and b:{b}')
    return a + b


add_few_number(a=6, b=7)
