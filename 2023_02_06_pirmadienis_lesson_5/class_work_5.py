
my_dict = {
    'Items':{
        'Electric_sockets':{
            'amount': 12
        },
        'Electronic_items':{
            'Transistors':{
                'KL_series':{
                        'KL565_type':{
                            'KL565A': 56,
                            'KL565B': 60
                        }
                },
                'KT_series':{
                        'KT315_type':{
                            'KT315B': 12,
                            'KT315C': 54
                        }
                }
                    
            }
            
        }
    }
}

print(my_dict['Items']['Electronic_items']['Transistors']['KT_series'])
