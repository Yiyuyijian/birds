# coding = utf-8
import xlrd


class Aves_China(object):
    def __init__(self,version:float):
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version{version}"
        excel = xlrd.open_workbook(f'.\\中国鸟类名录v{version}.xlsx')
        sheet = excel.sheet_by_index(0)
        self.__All_orders =  sheet.col_values(10,2)
        self.__All_families= sheet.col_values(8,2)
        self.__All_genuses = sheet.col_values(6,2)
        self.All_species = sheet.col_values(3,2)
    
    #目相关方法
    def orders(self):
        return list(set(self.__All_orders))

    def number_of_orders(self):
        return len(set(self.__All_orders))

    #科相关方法
    def families_in_order(self,order:str):
        assert isinstance(order,str),f'what you input is not a "str"' 
        assert order in self.orders(),f'There is no order named "{order}"'
        temp=[family for i,family in enumerate(self.__All_families) if self.__All_orders[i]==order]
        return list(set(temp))

    def number_of_families(self,order=None):
        if order==None:
            return len(set(self.__All_families))
        assert order in self.orders(),f'There is no order named "{order}"'
        return len(self.families_in_order(order))

    def search_families(self,keywords:str):
        '''
        retrun a list of bird families which contains the "keywords"
        '''
        family_list = set(self.__All_families)
        return [family for family in family_list if keywords in family]

    #属相关方法
    def genuses_in_family(self,family:str):
        assert family in self.__All_families,f'There is no family named "{family}"'
        temp=[genus for i,genus in enumerate(self.__All_genuses) if self.__All_families[i]==family]
        return list(set(temp))

    def number_of_genuses(self,family=None):
        if family==None:
            return len(set(self.__All_genuses))
        assert family in self.__All_families,f'There is no family named "{family}"'
        return len(self.genuses_in_family(family))

    def search_genuses(self,keywords:str):
        '''
        retrun a list of bird genuses which contains the "keywords"
        '''
        genus_list = set(self.__All_genuses)
        return [genus for genus in genus_list if keywords in genus]

    #种相关方法
    def species_in_genus(self,genus:str):
        assert genus in self.__All_genuses,f'There is no genus named "{genus}"'
        return [species for i,species in enumerate(self.All_species) if self.__All_genuses[i]==genus]

    def number_of_species(self,genus=None):
        if genus==None:
            return len(self.All_species)
        assert genus in self.__All_genuses,f'There is no genus named "{genus}"'
        return len(self.species_in_genus(genus))

    def search_species(self,keywords:str):
        '''
        retrun a list of bird species which contains the "keywords"
        '''
        return [species for species in self.All_species if keywords in species]
       
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
        self.scientific_names  =     sheet.cell_value(number+1,5)
        self.its_genus         =     sheet.cell_value(number+1,6)
        self.scientific_genus  =     sheet.cell_value(number+1,7)
        self.its_family        =     sheet.cell_value(number+1,8)
        self.scientific_family =     sheet.cell_value(number+1,9)
        self.its_order         =     sheet.cell_value(number+1,10)
        self.scientific_order  =     sheet.cell_value(number+1,11)

    @staticmethod
    def by_code(version:float,number:int):
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version{version}"        
        return Bird_species(version,number)

    @staticmethod
    def by_name_exactly(version:float,bird_name:str):
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version{version}" 
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
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version{version}"
        aves = Aves_China(version)
        #a list of bird names which include "keyword"
        splist = aves.search_species(keyword)
        for i,name in enumerate(splist):
            #convert a bird name to a instance of class "Bird_species()"
            splist[i] = Bird_species.by_name_exactly(version,name)
        return splist

if __name__=='__main__':
    b = Bird_species.by_code(3.0,45)
    print(b.Chinese_name)
        
