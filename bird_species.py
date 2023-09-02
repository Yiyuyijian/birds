from aves import Aves_China
import xlrd


class Bird_species(object):
    '''
    Creat an instance of bird species via its code number or name.
    '''
    def __init__(self,version:float,number:int):
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version{version}"
        excel=xlrd.open_workbook(f'.\\中国鸟类名录v{version}.xlsx')
        sheet=excel.sheet_by_index(0)
        assert 1<=number<=sheet.nrows-2,f"Please input a number between 1 and {sheet.nrows-2}!"
        self.code_number       =     int(sheet.cell_value(number+1,0))
        self.wild_code         =     sheet.cell_value(number+1,1)
        self.IUCN              =     sheet.cell_value(number+1,2)
        self.Chinese_name      =     sheet.cell_value(number+1,3)
        self.English_name      =     sheet.cell_value(number+1,4)
        self.scientific_name   =     sheet.cell_value(number+1,5)
        self.its_genus         =     sheet.cell_value(number+1,6)
        self.scientific_genus  =     sheet.cell_value(number+1,7)
        self.its_family        =     sheet.cell_value(number+1,8)
        self.scientific_family =     sheet.cell_value(number+1,9)
        self.its_order         =     sheet.cell_value(number+1,10)
        self.scientific_order  =     sheet.cell_value(number+1,11)

    @staticmethod
    def by_code(version:float,number:int):
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version {version}"        
        return Bird_species(version,number)

    @staticmethod
    def by_name_exactly(version:float,bird_name:str):
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version {version}" 
        aves = Aves_China(version)       
        assert bird_name in aves.All_species,f'There is no bird named "{bird_name}",please checkout!'     
        num = aves.All_species.index(bird_name)+1
        return Bird_species(version,num)

    @staticmethod
    def by_name_fuzzily(version:float,keyword:str):
        '''
        A fuzzy bird name was given.
        return a list of instances of class "Bird_species()"
        '''
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version {version}"
        aves = Aves_China(version)
        #a list of bird names which include "keyword"
        splist = aves.search_species(keyword)
        for name in splist:
            #convert a bird name to a instance of class "Bird_species()"
            bird = Bird_species.by_name_exactly(version,name)
            yield bird
        #return splist
    
if __name__ == "__main__":
    bs = Bird_species.by_name_fuzzily(10.0,"鹊")
    
    