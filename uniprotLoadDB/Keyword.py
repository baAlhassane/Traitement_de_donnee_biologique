# coding: utf8
'''
Created on 15 janv. 2019
Classe Keyword : mots cl�s de la base uniprotLoadDB
   Attributs :
      - kwId : keyword id
      - kwLabel : keyword label
@author: Sarah Cohen Boulakia
'''
class Keyword:

    # Parametre de classe utilise pour dire si les Keyword doivent etre inseres 
    # en base quand insertDB est appele
    DEBUG_INSERT_DB = True
    
    def __init__(self, kwId, kwLabel):
        self._kwId = kwId
        self._kwLabel = kwLabel
    
    
    '''
    Si le mot cle n'existe pas, ajout en base.
    @param curDb: Curseur sur la base de donnees oracle 
    @return N/A
    '''    
    def insertDB (self, curDB):
        curDB.prepare ("SELECT kw_id " \
                                + " FROM keywords " \
                                + " WHERE kw_id=:kwId")
        curDB.execute (None, {'kw_id': self._kwId })
        raw = curDB.fetchone ()
        if raw == None:
            if Keyword.DEBUG_INSERT_DB:
                #### TODO : Insérer le keyword s'il n'existe pas
                #### Cf. exemple de la classe Gene si besoin
                curDB.prepare("INSERT INTO keywords" \
                              +"(kw_id,kw_label)"\
                              +"VALUES"\
                              +"(:kw_id,kw_label)")##fin prepare 
                ####          ####
                curDB.execute(None,{'kw_id':self._kwId, 'kw_label':self._kwLabel})
                #### FIN TODO ####

