# coding = utf-8
import xlrd


class Aves_China(object):
    def __init__(self,version:float):
        '''The version must be one of 2.2, 3.0, 4.0, 5.0, 7.0, 8.0, 9.0, 10.0'''
        assert version in [2.2,3.0,4.0,5.0,7.0,8.0,9.0,10.0],f"There is no version {version}"
        excel = xlrd.open_workbook(f'.\\中国鸟类名录v{version}.xlsx')
        sheet = excel.sheet_by_index(0)
        self.__All_orders =  sheet.col_values(10,2)
        self.__All_families= sheet.col_values(8, 2)
        self.__All_genuses = sheet.col_values(6, 2)
        self.All_species  =  sheet.col_values(3, 2)
    
    #目相关方法
    def orders(self):
        return list(set(self.__All_orders))

    def number_of_orders(self):
        return len(set(self.__All_orders))

    #科相关方法
    def families_in_order(self,order:str):
        assert isinstance(order,str),f'what you input is not a string'
        assert order in self.orders(),f'There is no order named "{order}"'
        temp=[family for i,family in enumerate(self.__All_families) if self.__All_orders[i]==order]
        return list(set(temp))

    def number_of_families(self,order=None):
        if order==None:
            return len(set(self.__All_families))
        return len(self.families_in_order(order))

    def search_families(self,keywords:str):
        '''
        retrun a list of bird families which contains the "keywords"
        '''
        family_list = set(self.__All_families)
        return [family for family in family_list if keywords in family]

    #属相关方法
    def genuses_in_family(self,family:str):
        assert isinstance(family,str),f'what you input is not a string'
        assert family in self.__All_families,f'There is no family named "{family}"'
        temp=[genus for i,genus in enumerate(self.__All_genuses) if self.__All_families[i]==family]
        return list(set(temp))

    def number_of_genuses(self,family=None):
        if family==None:
            return len(set(self.__All_genuses))
        return len(self.genuses_in_family(family))

    def search_genuses(self,keywords:str):
        '''
        retrun a list of bird genuses which contains the "keywords"
        '''
        genus_list = set(self.__All_genuses)
        return [genus for genus in genus_list if keywords in genus]

    #种相关方法
    def species_in_genus(self,genus:str):
        assert isinstance(genus,str),f'what you input is not a string'
        assert genus in self.__All_genuses,f'There is no genus named "{genus}"'
        return [species for i,species in enumerate(self.All_species) if self.__All_genuses[i]==genus]

    def number_of_species(self,genus=None):
        if genus==None:
            return len(self.All_species)
        return len(self.species_in_genus(genus))

    def search_species(self,keywords:str):
        '''
        retrun a list of bird species which contains the "keywords"
        '''
        return [species for species in self.All_species if keywords in species]
       


if __name__=='__main__':
    a = Aves_China(10.0)
    #print(a.orders())
    #print(a.families_in_order("雀形目"))
    #print(a.genuses_in_family("王鹟科"))
    #print(a.species_in_genus("寿带属"))
    #print(a.number_of_orders())
    #print(a.number_of_families("雀形目"))
    #print(a.number_of_genuses("王鹟科"))
    #print(a.number_of_species("寿带属"))
    #print(a.search_families("鹟"))
    #print(a.search_genuses("鸲"))
    print(a.search_species("黑"))

        
