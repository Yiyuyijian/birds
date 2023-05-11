# -*- coding: utf-8 -*-
import xlrd
import tkinter.messagebox
class Aves_China(object):
    def __init__(self,version):
        excel = xlrd.open_workbook(f'.\\中国鸟类名录{version}.xlsx')
        sheet = excel.sheet_by_index(0)
        self.__All_orders=sheet.col_values(10,2)
        self.__All_families=sheet.col_values(8,2)
        self.__All_genuses=sheet.col_values(6,2)
        self.All_species=sheet.col_values(3,2)
    
    #目相关方法
    def orders(self):
        return list(set(self.__All_orders))

    def norder(self):
        return len(set(self.__All_orders))

    #科相关方法
    def families_in_order(self,order):
        assert order in self.orders(),"Please input the right order name"
        temp=[family for i,family in enumerate(self.__All_families) if self.__All_orders[i]==order]
        return list(set(temp))

    def nfamilies(self,order):
        return len(self.families_in_order(order))

    def nfamilies_all(self):
        return len(set(self.__All_families))

    def search_families(self,keywords:str):
        '''
        retrun a list of bird families which contains the "keywords"
        '''
        family_list = set(self.__All_families)
        return [family for family in family_list if keywords in family]

    #属相关方法
    def genus_in_family(self,family):
        temp=[genus for i,genus in enumerate(self.__All_genuses) if self.__All_families[i]==family]
        return list(set(temp))

    def ngenuses(self,family):
        return len(self.genus_in_family(family))
    
    def ngenuses_all(self):
        return len(set(self.__All_genuses))

    def search_genuses(self,keywords:str):
        '''
        retrun a list of bird genuses which contains the "keywords"
        '''
        genus_list = set(self.__All_genuses)
        return [genus for genus in genus_list if keywords in genus]

    #种相关方法
    def species_in_genus(self,genus):
        return [species for i,species in enumerate(self.All_species) if self.__All_genuses[i]==genus]

    def nspecies(self,genus):
        return len(self.species_in_genus(genus))

    def nspecies_all(self):
        return len(self.All_species)

    def search_species(self,keywords:str):
        '''
        retrun a list of bird species which contains the "keywords"
        '''
        return [species for species in self.All_species if keywords in species]
       
class Bird_species(object):
    '''
    Creat an instance of bird species via its code number or name.
    '''
    def __init__(self,version,row):
        excel=xlrd.open_workbook(f'.\\中国鸟类名录{version}.xlsx')
        sheet=excel.sheet_by_index(0)
        self.code = sheet.cell(row,0).value
        self.wild_code = sheet.cell_value(row,1)
        self.IUCN = sheet.cell_value(row,2)
        self.Chinese_name = sheet.cell_value(row,3)
        self.English_name = sheet.cell_value(row,4)
        self.scientific_names = sheet.cell_value(row,5)
        self.its_genus = sheet.cell_value(row,6)
        self.scientific_genus = sheet.cell_value(row,7)
        self.its_family = sheet.cell_value(row,8)
        self.scientific_family = sheet.cell_value(row,9)
        self.its_order = sheet.cell_value(row,10)
        self.scientific_order = sheet.cell_value(row,11)

    @classmethod
    def species_by_code(cls,version,code_number:int):        
        try:
            assert 1<=code_number<=1468,"Please input a number between 1 and 1458!"
            
        except Exception as result:
            tkinter.messagebox.showwarning("Notice:",result)
            return
        return cls(version,code_number)

    @classmethod
    def species_by_name_exactly(cls,version,bird_name:str):
        aves = Aves_China(version)
        try:
            assert bird_name in aves.All_species,"You input a wrong name,please checkout!"
            num = aves.All_species.index(bird_name)+1
        except Exception as result:
            tkinter.messagebox.showwarning("Notice:",result)
        return cls(version,num)

    @classmethod
    def species_by_name_fuzzily(cls,version,keyword:str):
        '''
        A fuzzy bird name was given.
        return a list of instances of class "Bird_species()"
        '''
        aves = Aves_China(version)
        #a list of bird names which include "keyword"
        splist = aves.search_species(keyword)
        for i,name in enumerate(splist):
            #convert a bird name to a instance of class "Bird_species()"
            splist[i] = cls.species_by_name_exactly(version,name)
        return splist

if __name__=='__main__':
    av2=Aves_China("v2.2")
    av3=Aves_China("v3.0")
    av4=Aves_China("v4.0")
    av5=Aves_China("v5.0")
    print(av2.nfamilies("雀形目"))




    

        



    
        
