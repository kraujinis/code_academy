# Write a function that moves all elements of one type to the end of the list:
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

import logging

logging.basicConfig(level=logging.DEBUG, filename='data.log',
                    filemode='a', format='%(asctime)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def move_to(take_list: list) -> None:
    logging.info(f"Input \"take_list\" in function : {take_list}")
    set_list = []
    arranged_list = []
    try:
        if len(take_list) == 0:
            logging.error(f"Input \"take_list\" in function is empty : {take_list}")
            
        else:
            for i in take_list:
                if take_list.count(i) > 1:
                    arranged_list.append(i)
                else:
                    set_list.append(i)
    except Exception as e:
        logging.error(f"Error in function move_to {e}")

    arranged_list.sort(reverse=True)
    logging.info(f"Sorted list of more then one unique value in value entered in function : {arranged_list}")
    set_list.extend(arranged_list)
    logging.info(f"Final output (list of unique values joined with sorted list):  {set_list}")


if __name__ == '__main__':

    array = []

    move_to(array)
