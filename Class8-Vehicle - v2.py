#2 - Write an algorithm (Vehicles.py) that, from reading and storing in vectors the commercial value 
# of 20 vehicles and the type (family (1), public transportation (2), load (3)), calculate the value based on:
#   • For vehicles with a value greater than 100 million, charge VAT of 20%, for others VAT is 16%
#   • For vehicles type 1, with value up to 50 million, apply a discount equivalent to 50% of the VAT charged
#   • For vehicles type 2 and 3, with a value higher than 80 million, apply an additional cost of 5%
#   • For all vehicles, if the final value is less than 80 million, apply an additional discount of 5% of 
#     the commercial value
class Vehicle:
    Type=""
    CommercialValue=0.0
    FinalPrice=0.0
    def __init__(self, value):
        self.CommercialValue = value
        self.FinalPrice = value
        self.VATCharged =0.0
        self.Discount =0.0
        self.AdditionalCost =0.0

    def __str__(self):
        return f"({self.Type} {self.CommercialValue} {self.FinalPrice})"
    
    def __repr__(self):
        return f"({self.Type} {self.CommercialValue} {self.FinalPrice})"
    
    def getVAT(self):        
        if(self.CommercialValue>100):
            self.VATCharged =  self.CommercialValue*0.2
        else:
            self.VATCharged =  self.CommercialValue*0.16
        return self.VATCharged
    
    def getDiscount(self):
        return self.Discount  
        
    def getAdditionalCost(self):
        return self.AdditionalCost
        
    def getFinalPrice(self):
        self.FinalPrice = self.CommercialValue + self.getVAT() +self.getDiscount()
        if(self.FinalPrice<80):
            self.FinalPrice = round(self.FinalPrice + self.CommercialValue*0.05,2)
        return self.FinalPrice

        
class VehicleType1(Vehicle):
    def __init__(self, value):
        super().__init__(value)    
        self.Type = 1

    def getDiscount(self):
        if(self.CommercialValue>=50):
            self.Discount = self.getVAT() *0.5
        return self.Discount

class VehicleType2(Vehicle):
    def __init__(self, value):
        super().__init__(value)    
        self.Type = 2

    def getAdditionalCost(self):
        if(self.CommercialValue >80):
            self.AdditionalCost = self.CommercialValue*0.05

class VehicleType3(Vehicle):
    def __init__(self, value):
        super().__init__(value)    
        self.Type = 3

    def getAdditionalCost(self):
        if(self.CommercialValue >=80):
            self.AdditionalCost = self.CommercialValue*0.05

def createVehicle(type, value):
    if type==1:
        return VehicleType1(value)
    elif type==2:
        return VehicleType2(value)
    elif type==3:
        return VehicleType3(value)
    else:
        return Vehicle()
    
import pandas
def calFinalVehiclePrice(file):
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

l = calFinalVehiclePrice("VehicleData.xlsx")
#print(l)