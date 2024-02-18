import pandas
def calFinalVehiclePrice(file)
    vehicle_listl=[]
    price_list=[]
    try:
        dataframe = pandas.read_excel(file)
        
        # Iterate the loop to read the cell values
        for row in range(0, dataframe.shape[0]):
            type = dataframe.iloc[row,1]
            value= dataframe.iloc[row,2]
            vehicle = createVehicle(type,value)
            price_list.append(vehicle.getFinalPrice())
            print(vehicle)
            vehicle_listl.append(vehicle)
        dataframe.insert(3,"Final Price", price_list)
        try:
            with pandas.ExcelWriter(file,engine="openpyxl",if_sheet_exists='replace', mode='a') as writer:
                dataframe.to_excel(writer, sheet_name="sheet2", index=False)
        except PermissionError:
            print(f"Error: Permission denied. Please make sure you have write access to the file '{file}'.")
            exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit()
        return vehicle_listl
    except FileNotFoundError:
        print(f"Error: File '{file}' not found. Please provide the correct file path.")
        exit()
    except pandas.errors.EmptyDataError:
        print(f"Error: File '{file}' is empty. Please make sure it contains data.")
        exit()
