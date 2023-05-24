#-*- coding: utf-8 -*-

#------------------------------------------------------------
from __future__ import print_function
#------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------
class bangla:
    iden                    =    "bangla"
    # for grapheme decomp
    vowel_diacritics        =    ['া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ']
    consonant_diacritics    =    ['ঁ']
    connector               =    '্'
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------

class gujrati:
    iden                   =    "gujrati"
    # for grapheme decomp
    vowel_diacritics       =    ['ૢ', 'ૣ', 'ૃ', 'ૄ', 'ા', 'િ', 'ી', 'ુ', 'ૂ', 'ૃ', 'ૄ', 'ૅ', 'ે', 'ૈ', 'ૉ', 'ો', 'ૌ' ] 
    consonant_diacritics   =    ['ૺ', 'ૻ', 'ૼ', '૽', '૾', '૿', 'ઁ', 'ં', 'ઃ']
    connector              =    '્'
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------

class panjabi:
    iden                   =    "panjabi"
    # for grapheme decomp
    vowel_diacritics       =    ['ੀ', 'ੂ', 'ਿ', 'ੁ', 'ੇ', 'ੋ', 'ੈ', 'ੌ', 'ਾ' ]
    consonant_diacritics   =    ['ੰ', 'ਂ','ੱ', 'ੑ', 'ੵ', 'ਃ']# last one from sikh holy book. # second one also historical
    connector              =    '੍' 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------

class odiya:
    iden                   =    "odiya"
    # for grapheme decomp
    vowel_diacritics       =    ['ି', 'ୀ', 'ୁ', 'ୂ', 'େ', 'ୋ', 'ା', 'ୈ', 'ୌ', 'ୖ', 'ୗ' , 'ୃ', 'ୄ', 'ୢ', 'ୣ'] 
    consonant_diacritics   =    ['ଂ', 'ଁ', 'ଃ'] 
    connector              =    '୍' 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------

class tamil:
    iden                   =    "tamil"
    # for grapheme decomp
    vowel_diacritics       =    ['ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ொ', 'ோ', 'ை', 'ௌ']
    consonant_diacritics   =    [] # not used much
    connector              =    '்' # yes, this shit is Tamil hoshonto -_- 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------

class malyalam:
    iden                   =    "malyalam"
    # for grapheme decomp
    vowel_diacritics       =    ['െ', 'േ',  'ൈ', 'ൊ', 'ോ', 'ൌ', 'ി', 'ീ', 'ു', 'ൂ', 'ാ', 'ൗ', 'ൃ']
    consonant_diacritics   =    ['ഃ', 'ം', 'ൎ'] # not used much
    connector              =    '്' # yes, this shit is malayalam hoshonto -_- 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------

class hindi:
    iden                   =    "hindi"
    # for grapheme decomp
    vowel_diacritics       =    ['ि', 'ी', 'ु', 'ू', 'े', 'ो', 'ै', 'ौ', 'ा', 'ृ' ,  'ॅ', 'ॉ']
    consonant_diacritics   =    ['ः', 'ं', 'ँ'] 
    connector              =    '्'
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------- add all language info-------------------------------------------------------------
languages={}
languages["bangla"]=bangla
languages["malyalam"]=malyalam
languages["tamil"]=tamil
languages["gujrati"]=gujrati
languages["panjabi"]=panjabi
languages["odiya"]=odiya
languages["hindi"]=hindi