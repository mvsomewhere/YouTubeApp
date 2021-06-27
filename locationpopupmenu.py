from kivymd.uix.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):

    def __init__(self, market_data):
        super().__init__()
        headers = "FMID,MarketName,Website,Facebook,Twitter,Youtube,OtherMedia,street,city,County,State,zip,Season1Date,Season1Time,Season2Date,Season2Time,Season3Date,Season3Time,Season4Date,Season4Time,x,y,Location,Credit,WIC,WICcash,SFMNP,SNAP,Organic,Bakedgoods,Cheese,Crafts,Flowers,Eggs,Seafood,Herbs,Vegetables,Honey,Jams,Maple,Meat,Nursery,Nuts,Plants,Poultry,Prepared,Soap,Trees,Wine,Coffee,Beans,Fruits,Grains,Juices,Mushrooms,PetFood,Tofu,WildHarvested,updateTime"
        headers = headers.split(',')
        for i in range (len(headers)):
            attribute_name = headers[i]
            attribute_value = market_data[i]
            setattr(self, attribute_name, attribute_value)#here self is LocationPopupMenu, so attribute_name is an attribute that is going to be found there(or in it's parent class)

        #set all of the fields of market data