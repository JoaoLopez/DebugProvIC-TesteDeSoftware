from debugprov.parameter import Parameter
from debugprov.validity import Validity
import json
import os

class Node:
    
    def __init__(self, ev_id, code_component_id, retrn, name, parent):
        self.ev_id = ev_id
        self.code_component_id = code_component_id
        self.retrn = retrn #Não precisa ser folha!
        self.name = name
        self.parent = parent
        self.childrens = []
        #print(self.childrens)
        self.validity = Validity.UNKNOWN  #Retorna se o nó está correto.
        self.params = [[0], []]
        self.indext=0

    def has_childrens(self):
        return len(self.childrens) > 0

    def has_childrens_with_validity(self, validity:Validity):   
        for c in self.childrens:
            if c.validity is validity:
                return True
        return False 
    
    def all_childrens_are_valid(self):
        for chd in self.childrens:
            if chd.validity is not Validity.VALID:
                return False
        return True

    def get_parameters(self, cursor):
        query = ("select CC.name, EV.repr as 'value' "
                 "from composition CMP "
                 "join code_component CC on CMP.part_id = CC.id "
                 "join evaluation EV on EV.code_component_id = CC.id "
                 "where CMP.whole_id = ? " 
                 "and CMP.type = ? ")
        for tupl in cursor.execute(query, [self.code_component_id, '*args']):
            self.params[1].append(Parameter(tupl[0], tupl[1]))
            #self.indext+=1
        print(self.params)
    
    def into_Json(self, answer):
        indx=lambda: dicio['pilhas'][self.name]
        file=os.environ.get("modulo")
        params=[{'str_name':str(x.name), 
                          #'type_name':str(type(x.name)), 
                          'str_value':str(x.value), 
                          'type_value':str(type(x.value))} for x in self.params]
        with open(file, 'r', encoding='utf-8') as json_file:
            dicio=json.load(json_file)
            if self.name in dicio['pilhas']:
                dicio['pilhas'][self.name]+=1
            else:
                dicio['pilhas'][self.name]=0
            #if len(params)>1:
            #    params=params[dicio['pilhas'][self.name]]
            thisNode={
            'ev_id': self.ev_id, 
            'code_component_id':self.code_component_id, 
            'retrn': self.retrn,
            'name': self.name,
            'answer': answer,
            'param_str': params[dicio['pilhas'][self.name]]
            '''param_str':[{'str_name':str(x.name), 
                          #'type_name':str(type(x.name)), 
                          'str_value':str(x.value), 
                          'type_value':str(type(x.value))} for x in self.params[::-1]][dicio['pilhas'].get(self.name)],
                          '''
            #'indext':float(self.params[0][0])
            #'indext':dicio['pilhas'].get(self.name),
            }
            
            dicio['params'][self.ev_id]=thisNode
        with open(file, 'w', encoding='utf-8') as json_file:    
            json.dump(dicio, json_file, indent=4)
        self.params[0][0]+=1

    def get_name(self):
        #print(self)
        return "{} {}".format(self.ev_id, self.name)
    
    def __repr__(self):
        msg="{} {}".format(self.ev_id, self.name)
        if len(self.childrens):
            msg+=str([f'{x.ev_id} {x.name}' for x in self.childrens])
        
        msg+= 'retorno + =' + self.retrn
        #for x in self.childrens:
        #    #msg+=x.name
        return msg
    