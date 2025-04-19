# In views/__init__.py


from .A000_view_Directory import directory


from .A1_view_home_old import home_view_old
from .A1_view_home_new import home_view_new

from .A02_view_browse import browse_view
from .A002_view_auora import auora_view

from .A3_view_preview import preview_view
from .B4_view_csv_eventLog import event_log
from .B5_view_csv_otherEntities import otherEntities
from .B6_view_csv_entityRel import entityRel
from .B7_view_csv_activityProperties import activityProperties
from .B8_view_csv_Domain import Domain
from .B9_view_csv_ICD import ICD
from .B10_view_csv_SctNode import SctNode
from .B11_view_csv_SctRel import SctRel
from .B12_view_csv_DK1 import DK1
from .B13_view_csv_DK2 import  DK2
from .B14_view_csv_DK3 import DK3
from .B15_view_csv_DK4 import DK4
from .B16_view_csv_DK5 import DK5
from .B17_view_csv_DK61 import DK61
from .B18_view_csv_DK62 import DK62
from .B19_view_csv_DK7 import DK7

from .C18_view_csv_Downloading import downloadingCsv
from .C19_view_csv_Link import csvLinking

from .C20_view_neo4j_conv_EventLog import conv_EvnetLog
from .C21_view_neo4j_eventLog import eventLogNeo4jFunc

from .C22_view_neo4j_conv_otherEntities import conv_otherEntities
from .C23_view_neo4j_otherEntities import otherEntitiesNeo4jFunc

from .C24_view_neo4j_conv_entityRel import conv_entityRel
from .C25_view_neo4j_entityRel import entityRelNeo4jFunc

from .C26_view_neo4j_conv_activityProperties import conv_activityProperties
from .C27_view_neo4j_activityProperties import activityPropertiesNeo4jFunc

from .C28_view_neo4j_conv_Domain import conv_Domain
from .C29_view_neo4j_Domain import DomainNeo4jFunc

from .C30_view_neo4j_conv_ICD import conv_ICD
from .C31_view_neo4j_ICD import ICDNeo4jFunc

from .C32_view_neo4j_conv_SctNode import conv_SctNode
from .C33_view_neo4j_SctNode import SctNodeNeo4jFunc

from .C34_view_neo4j_conv_SctRel import conv_SctRel
from .C35_view_neo4j_SctRel import SctRelNeo4jFunc

from .C36_view_neo4j_conv_DK1 import conv_DK1
from .C37_view_neo4j_DK1 import DK1Neo4jFunc

from .C38_view_neo4j_conv_DK2 import conv_DK2
from .C39_view_neo4j_DK2 import  DK2Neo4jFunc

from .C40_view_neo4j_conv_DK3 import conv_DK3
from .C41_view_neo4j_DK3 import DK3Neo4jFunc

from .C42_view_neo4j_conv_DK4 import conv_DK4
from .C43_view_neo4j_DK4 import DK4Neo4jFunc

from .C44_view_neo4j_conv_DK5 import conv_DK5
from .C45_view_neo4j_DK5 import DK5Neo4jFunc

from .C46_view_neo4j_conv_DK6 import conv_DK6
from .C47_view_neo4j_DK6 import DK6Neo4jFunc

from .C48_view_neo4j_conv_DK7 import conv_DK7
from .C49_view_neo4j_DK7 import DK7Neo4jFunc

from .D50_view_neo4j_conv_BuildingQuery import conv_BuildingQuery
from .D51_view_BuildingQuery import queryLister


from .E52_view_neo4j_conv_DFG import conv_DFG
from .E53_view_DFG import DFG

