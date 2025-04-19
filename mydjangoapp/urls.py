
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from myapp.views.A0_view_welcome import welcome_view

from myapp.views.A0_view_singUpIn import signPage
from myapp.views.A0_view_successSignUp import signup_success
from myapp.views.A0_view_pendingSignUp import approval_pending


from myapp.views.A000_view_Directory import directory


from myapp.views.A1_view_home_old import home_view_old
from myapp.views.A1_view_home_new import home_view_new
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step1_01
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step1_02
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step1_03
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step1_04
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step1_05
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step1_06

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_1
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_2
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_3
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_4
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_5
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_6
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_7
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_8

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_09
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_10
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_11
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_12
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_13
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_14
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_15
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_16

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_17
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_18
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_19
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_20
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_21
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_22
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_23
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_24
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_25
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_26
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_27
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_28

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_29
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_30
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_31
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_32
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_33
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_34
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_35
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_36
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_37
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_38
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_39
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_40

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_41
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_42
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_43
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_44
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_45
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_46
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_47
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_48
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_49
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_50
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_51
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_52

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_53
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step2_54

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_01
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_02
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_03
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_04
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_05
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_06
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_07
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_08
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_09

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step3_option

from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step4_01
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step4_02
from myapp.views.A1_view_home_new_resourseURL import serve_pdf_func_step4_03




from myapp.views.A02_view_browse import browse_view
from myapp.views.A002_view_auora import auora_view
from myapp.views.A3_view_preview import preview_view
from myapp.views.A3_view_preview import get_excel_data

from myapp.views.B4_view_csv_eventLog import event_log
from myapp.views.B5_view_csv_otherEntities import otherEntities
from myapp.views.B6_view_csv_entityRel import entityRel
from myapp.views.B7_view_csv_activityProperties import activityProperties
from myapp.views.B8_view_csv_Domain import Domain
from myapp.views.B9_view_csv_ICD import ICD
from myapp.views.B10_view_csv_SctNode import SctNode
from myapp.views.B11_view_csv_SctRel import SctRel
from myapp.views.B12_view_csv_DK1 import DK1
from myapp.views.B13_view_csv_DK2 import DK2
from myapp.views.B14_view_csv_DK3 import DK3
from myapp.views.B15_view_csv_DK4 import DK4
from myapp.views.B16_view_csv_DK5 import DK5
from myapp.views.B17_view_csv_DK61 import DK61
from myapp.views.B18_view_csv_DK62 import DK62
from myapp.views.B19_view_csv_DK7 import DK7

from myapp.views.C18_view_csv_Downloading import downloadingCsv
from myapp.views.C19_view_csv_Link import csvLinking

from myapp.views.C20_view_neo4j_conv_EventLog import conv_EvnetLog
from myapp.views.C21_view_neo4j_eventLog import eventLogNeo4jFunc
from myapp.views.C22_view_neo4j_conv_otherEntities import conv_otherEntities
from myapp.views.C23_view_neo4j_otherEntities import otherEntitiesNeo4jFunc
from myapp.views.C24_view_neo4j_conv_entityRel import conv_entityRel
from myapp.views.C25_view_neo4j_entityRel import entityRelNeo4jFunc
from myapp.views.C26_view_neo4j_conv_activityProperties import conv_activityProperties
from myapp.views.C27_view_neo4j_activityProperties import activityPropertiesNeo4jFunc
from myapp.views.C28_view_neo4j_conv_Domain import conv_Domain
from myapp.views.C29_view_neo4j_Domain import DomainNeo4jFunc
from myapp.views.C30_view_neo4j_conv_ICD import conv_ICD
from myapp.views.C31_view_neo4j_ICD import ICDNeo4jFunc
from myapp.views.C32_view_neo4j_conv_SctNode import conv_SctNode
from myapp.views.C33_view_neo4j_SctNode import SctNodeNeo4jFunc
from myapp.views.C34_view_neo4j_conv_SctRel import conv_SctRel
from myapp.views.C35_view_neo4j_SctRel import SctRelNeo4jFunc
from myapp.views.C36_view_neo4j_conv_DK1 import conv_DK1
from myapp.views.C37_view_neo4j_DK1 import DK1Neo4jFunc
from myapp.views.C38_view_neo4j_conv_DK2 import conv_DK2
from myapp.views.C39_view_neo4j_DK2 import DK2Neo4jFunc
from myapp.views.C40_view_neo4j_conv_DK3 import conv_DK3
from myapp.views.C41_view_neo4j_DK3 import DK3Neo4jFunc
from myapp.views.C42_view_neo4j_conv_DK4 import conv_DK4
from myapp.views.C43_view_neo4j_DK4 import DK4Neo4jFunc
from myapp.views.C44_view_neo4j_conv_DK5 import conv_DK5
from myapp.views.C45_view_neo4j_DK5 import DK5Neo4jFunc
from myapp.views.C46_view_neo4j_conv_DK6 import conv_DK6
from myapp.views.C47_view_neo4j_DK6 import DK6Neo4jFunc
from myapp.views.C48_view_neo4j_conv_DK7 import conv_DK7
from myapp.views.C49_view_neo4j_DK7 import DK7Neo4jFunc



from myapp.views.C20_view_neo4j_conv_EventLog_resourseURL import seve_jpegCKEG1
from myapp.views.C22_view_neo4j_conv_otherEntities_resourceURL import seve_jpegCKEG2
from myapp.views.C24_view_neo4j_conv_entityRel_resourceURL import seve_jpegCKEG3
from myapp.views.C26_view_neo4j_conv_activityProperties_resourceURL import seve_jpegCKEG4
from myapp.views.C28_view_neo4j_conv_Domain_resourceURL import seve_jpegCKEG5
from myapp.views.C30_view_neo4j_conv_ICD_resourceURL import seve_jpegCKEG6
from myapp.views.C32_view_neo4j_conv_SctNode_resourceURL import seve_jpegCKEG7
from myapp.views.C34_view_neo4j_conv_SctRel_resourceURL import seve_jpegCKEG8
from myapp.views.C36_view_neo4j_conv_DK1_resourceURL import seve_jpegCKEG9
from myapp.views.C38_view_neo4j_conv_DK2_resourceURL import seve_jpegCKEG10
from myapp.views.C40_view_neo4j_conv_DK3_resourceURL import seve_jpegCKEG11
from myapp.views.C42_view_neo4j_conv_DK4_resourceURL import seve_jpegCKEG12
from myapp.views.C44_view_neo4j_conv_DK5_resourceURL import seve_jpegCKEG13
from myapp.views.C46_view_neo4j_conv_DK6_resourceURL import seve_jpegCKEG14
from myapp.views.C48_view_neo4j_conv_DK7_resourceURL import seve_jpegCKEG15
from myapp.views.D50_view_neo4j_conv_BuildingQuery_resourceURL import seve_jpegCKEG16
from myapp.views.E52_view_neo4j_conv_DFG_resourceURL import seve_jpegCKEG17




from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ1_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ2_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ3_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ4_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ5_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ6_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ7_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ8_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ9_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ10_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ11_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ12_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ4_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ5_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ6_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ7_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ8_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ9_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ10_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ11_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ12_EventLog
from myapp.views.C23_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ1_otherEntities
from myapp.views.C23_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ2_otherEntities
from myapp.views.C23_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ3_otherEntities
from myapp.views.C23_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ4_otherEntities
from myapp.views.C23_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_svgQ4_otherEntities
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ1_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ2_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ3_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ4_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ5_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ6_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ7_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ8_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ9_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ10_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ11_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ12_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ3_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ6_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ7_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ8_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ9_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ10_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ11_entityRel
from myapp.views.C25_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ12_entityRel
from myapp.views.C27_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ1_activityProperties
from myapp.views.C27_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ2_activityProperties
from myapp.views.C27_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ3_activityProperties
from myapp.views.C27_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ4_activityProperties
from myapp.views.C27_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ5_activityProperties
from myapp.views.C27_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_svgQ4_activityProperties
from myapp.views.C27_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_svgQ5_activityProperties
from myapp.views.C29_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ1_Domain
from myapp.views.C29_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ2_Domain
from myapp.views.C29_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ3_Domain
from myapp.views.C29_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ4_Domain
from myapp.views.C29_view_neo4j_Domain_resourseURL import seve_neo4jQuery_svgQ4_Domain
from myapp.views.C31_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ1_ICD
from myapp.views.C31_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ2_ICD
from myapp.views.C31_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ3_ICD
from myapp.views.C31_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ4_ICD
from myapp.views.C31_view_neo4j_ICD_resourseURL import seve_neo4jQuery_svgQ4_ICD
from myapp.views.C33_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ1_sctNode
from myapp.views.C33_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ2_sctNode
from myapp.views.C33_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ3_sctNode
from myapp.views.C33_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ4_sctNode
from myapp.views.C33_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_svgQ4_sctNode
from myapp.views.C35_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_funcQ1_sctRel
from myapp.views.C35_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_funcQ2_sctRel
from myapp.views.C35_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_funcQ3_sctRel
from myapp.views.C35_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_svgQ2_sctRel
from myapp.views.C35_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_svgQ3_sctRel
from myapp.views.C41_view_neo4j_DK3_resourseURL import seve_neo4jQuery_funcQ1_DK3
from myapp.views.C41_view_neo4j_DK3_resourseURL import seve_neo4jQuery_funcQ2_DK3
from myapp.views.C41_view_neo4j_DK3_resourseURL import seve_neo4jQuery_svgQ2_DK3
from myapp.views.C43_view_neo4j_DK4_resourseURL import seve_neo4jQuery_funcQ1_DK4
from myapp.views.C43_view_neo4j_DK4_resourseURL import seve_neo4jQuery_funcQ2_DK4
from myapp.views.C43_view_neo4j_DK4_resourseURL import seve_neo4jQuery_svgQ2_DK4
from myapp.views.C45_view_neo4j_DK5_resourseURL import seve_neo4jQuery_funcQ1_DK5
from myapp.views.C45_view_neo4j_DK5_resourseURL import seve_neo4jQuery_funcQ2_DK5
from myapp.views.C45_view_neo4j_DK5_resourseURL import seve_neo4jQuery_funcQ3_DK5
from myapp.views.C45_view_neo4j_DK5_resourseURL import seve_neo4jQuery_svgQ2_DK5
from myapp.views.C45_view_neo4j_DK5_resourseURL import seve_neo4jQuery_svgQ3_DK5
from myapp.views.C47_view_neo4j_DK6_resourseURL import seve_neo4jQuery_funcQ1_DK6
from myapp.views.C47_view_neo4j_DK6_resourseURL import seve_neo4jQuery_funcQ2_DK6
from myapp.views.C47_view_neo4j_DK6_resourseURL import seve_neo4jQuery_svgQ2_DK6
from myapp.views.C49_view_neo4j_DK7_resourseURL import seve_neo4jQuery_funcQ1_DK7
from myapp.views.C49_view_neo4j_DK7_resourseURL import seve_neo4jQuery_funcQ2_DK7
from myapp.views.C49_view_neo4j_DK7_resourseURL import seve_neo4jQuery_svgQ2_DK7
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ1_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ2_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ3_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ4_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ5_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ6_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ7_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ8_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ9_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ10_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ11_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ12_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ13_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ14_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ15_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ16_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ17_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ18_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ19_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ20_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ21_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ22_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ3_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ4_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ5_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ6_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ7_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ8_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ9_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ10_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ11_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ12_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ13_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ14_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ15_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ16_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ17_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ18_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ19_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ20_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ21_Final
from myapp.views.D51_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ22_Final

from myapp.views.D50_view_neo4j_conv_BuildingQuery import conv_BuildingQuery
from myapp.views.D51_view_BuildingQuery import queryLister

from myapp.views.E52_view_neo4j_conv_DFG import conv_DFG
from myapp.views.E53_view_DFG import DFG
from myapp.views.E53_view_DFG_resourceURL import serve_pdf_func
from myapp.views.E53_view_DFG_resourceURL import serve_dot_func
from myapp.views.E53_view_DFG_resourceURL import serve_graphvizQuery_func
from myapp.views.E53_view_DFG_resourceURL import serve_neo4jQuery_func





urlpatterns = [

    path('', welcome_view, name='welcomeViewName'),

    path('admin/', admin.site.urls),

    path('login/', signPage, name='sign'),
    path('signup_success/', signup_success, name='signup_success'),
    path('approval_pending/', approval_pending, name='approval_pending'),






    path('directory/', directory, {'path': ''}, name='directory'),

    re_path(r'^files/(?P<path>.*)$', directory, name='directory'),

    path('homePage/', home_view_old, name='home'),

    path('homePageStep1_01/', serve_pdf_func_step1_01, name='serve_pdf_func_step1_01_name'),
    path('homePageStep1_02/', serve_pdf_func_step1_02, name='serve_pdf_func_step1_02_name'),
    path('homePageStep1_03/', serve_pdf_func_step1_03, name='serve_pdf_func_step1_03_name'),
    path('homePageStep1_04/', serve_pdf_func_step1_04, name='serve_pdf_func_step1_04_name'),
    path('homePageStep1_05/', serve_pdf_func_step1_05, name='serve_pdf_func_step1_05_name'),
    path('homePageStep1_06/', serve_pdf_func_step1_06, name='serve_pdf_func_step1_06_name'),

    path('homePageStep2_1/', serve_pdf_func_step2_1, name='serve_pdf_func_step2_1_name'),
    path('homePageStep2_2/', serve_pdf_func_step2_2, name='serve_pdf_func_step2_2_name'),
    path('homePageStep2_3/', serve_pdf_func_step2_3, name='serve_pdf_func_step2_3_name'),
    path('homePageStep2_4/', serve_pdf_func_step2_4, name='serve_pdf_func_step2_4_name'),
    path('homePageStep2_5/', serve_pdf_func_step2_5, name='serve_pdf_func_step2_5_name'),
    path('homePageStep2_6/', serve_pdf_func_step2_6, name='serve_pdf_func_step2_6_name'),
    path('homePageStep2_7/', serve_pdf_func_step2_7, name='serve_pdf_func_step2_7_name'),
    path('homePageStep2_8/', serve_pdf_func_step2_8, name='serve_pdf_func_step2_8_name'),

    path('homePageStep2_09/', serve_pdf_func_step2_09, name='serve_pdf_func_step2_09_name'),
    path('homePageStep2_10/', serve_pdf_func_step2_10, name='serve_pdf_func_step2_10_name'),
    path('homePageStep2_11/', serve_pdf_func_step2_11, name='serve_pdf_func_step2_11_name'),
    path('homePageStep2_12/', serve_pdf_func_step2_12, name='serve_pdf_func_step2_12_name'),
    path('homePageStep2_13/', serve_pdf_func_step2_13, name='serve_pdf_func_step2_13_name'),
    path('homePageStep2_14/', serve_pdf_func_step2_14, name='serve_pdf_func_step2_14_name'),
    path('homePageStep2_15/', serve_pdf_func_step2_15, name='serve_pdf_func_step2_15_name'),
    path('homePageStep2_16/', serve_pdf_func_step2_16, name='serve_pdf_func_step2_16_name'),

    path('homePageStep2_17/', serve_pdf_func_step2_17, name='serve_pdf_func_step2_17_name'),
    path('homePageStep2_18/', serve_pdf_func_step2_18, name='serve_pdf_func_step2_18_name'),
    path('homePageStep2_19/', serve_pdf_func_step2_19, name='serve_pdf_func_step2_19_name'),
    path('homePageStep2_20/', serve_pdf_func_step2_20, name='serve_pdf_func_step2_20_name'),
    path('homePageStep2_21/', serve_pdf_func_step2_21, name='serve_pdf_func_step2_21_name'),
    path('homePageStep2_22/', serve_pdf_func_step2_22, name='serve_pdf_func_step2_22_name'),
    path('homePageStep2_23/', serve_pdf_func_step2_23, name='serve_pdf_func_step2_23_name'),
    path('homePageStep2_24/', serve_pdf_func_step2_24, name='serve_pdf_func_step2_24_name'),
    path('homePageStep2_25/', serve_pdf_func_step2_25, name='serve_pdf_func_step2_25_name'),
    path('homePageStep2_26/', serve_pdf_func_step2_26, name='serve_pdf_func_step2_26_name'),
    path('homePageStep2_27/', serve_pdf_func_step2_27, name='serve_pdf_func_step2_27_name'),
    path('homePageStep2_28/', serve_pdf_func_step2_28, name='serve_pdf_func_step2_28_name'),

    path('homePageStep2_29/', serve_pdf_func_step2_29, name='serve_pdf_func_step2_29_name'),
    path('homePageStep2_30/', serve_pdf_func_step2_30, name='serve_pdf_func_step2_30_name'),
    path('homePageStep2_31/', serve_pdf_func_step2_31, name='serve_pdf_func_step2_31_name'),
    path('homePageStep2_32/', serve_pdf_func_step2_32, name='serve_pdf_func_step2_32_name'),
    path('homePageStep2_33/', serve_pdf_func_step2_33, name='serve_pdf_func_step2_33_name'),
    path('homePageStep2_34/', serve_pdf_func_step2_34, name='serve_pdf_func_step2_34_name'),
    path('homePageStep2_35/', serve_pdf_func_step2_35, name='serve_pdf_func_step2_35_name'),
    path('homePageStep2_36/', serve_pdf_func_step2_36, name='serve_pdf_func_step2_36_name'),
    path('homePageStep2_37/', serve_pdf_func_step2_37, name='serve_pdf_func_step2_37_name'),
    path('homePageStep2_38/', serve_pdf_func_step2_38, name='serve_pdf_func_step2_38_name'),
    path('homePageStep2_39/', serve_pdf_func_step2_39, name='serve_pdf_func_step2_39_name'),
    path('homePageStep2_40/', serve_pdf_func_step2_40, name='serve_pdf_func_step2_40_name'),

    path('homePageStep2_41/', serve_pdf_func_step2_41, name='serve_pdf_func_step2_41_name'),
    path('homePageStep2_42/', serve_pdf_func_step2_42, name='serve_pdf_func_step2_42_name'),
    path('homePageStep2_43/', serve_pdf_func_step2_43, name='serve_pdf_func_step2_43_name'),
    path('homePageStep2_44/', serve_pdf_func_step2_44, name='serve_pdf_func_step2_44_name'),
    path('homePageStep2_45/', serve_pdf_func_step2_45, name='serve_pdf_func_step2_45_name'),
    path('homePageStep2_46/', serve_pdf_func_step2_46, name='serve_pdf_func_step2_46_name'),
    path('homePageStep2_47/', serve_pdf_func_step2_47, name='serve_pdf_func_step2_47_name'),
    path('homePageStep2_48/', serve_pdf_func_step2_48, name='serve_pdf_func_step2_48_name'),
    path('homePageStep2_49/', serve_pdf_func_step2_49, name='serve_pdf_func_step2_49_name'),
    path('homePageStep2_50/', serve_pdf_func_step2_50, name='serve_pdf_func_step2_50_name'),
    path('homePageStep2_51/', serve_pdf_func_step2_51, name='serve_pdf_func_step2_51_name'),
    path('homePageStep2_52/', serve_pdf_func_step2_52, name='serve_pdf_func_step2_52_name'),

    path('homePageStep2_53/', serve_pdf_func_step2_53, name='serve_pdf_func_step2_53_name'),
    path('homePageStep2_54/', serve_pdf_func_step2_54, name='serve_pdf_func_step2_54_name'),

    path('homePageStep3_01/', serve_pdf_func_step3_01, name='serve_pdf_func_step3_01_name'),
    path('homePageStep3_02/', serve_pdf_func_step3_02, name='serve_pdf_func_step3_02_name'),
    path('homePageStep3_03/', serve_pdf_func_step3_03, name='serve_pdf_func_step3_03_name'),
    path('homePageStep3_04/', serve_pdf_func_step3_04, name='serve_pdf_func_step3_04_name'),
    path('homePageStep3_05/', serve_pdf_func_step3_05, name='serve_pdf_func_step3_05_name'),
    path('homePageStep3_06/', serve_pdf_func_step3_06, name='serve_pdf_func_step3_06_name'),
    path('homePageStep3_07/', serve_pdf_func_step3_07, name='serve_pdf_func_step3_07_name'),
    path('homePageStep3_08/', serve_pdf_func_step3_08, name='serve_pdf_func_step3_08_name'),
    path('homePageStep3_09/', serve_pdf_func_step3_09, name='serve_pdf_func_step3_09_name'),

    path('homePageStep3_option/', serve_pdf_func_step3_option, name='serve_pdf_func_step3_option_name'),

    path('homePageStep4_01/', serve_pdf_func_step4_01, name='serve_pdf_func_step4_01_name'),
    path('homePageStep4_02/', serve_pdf_func_step4_02, name='serve_pdf_func_step4_02_name'),
    path('homePageStep4_03/', serve_pdf_func_step4_03, name='serve_pdf_func_step4_03_name'),






    path('browseExcel/', browse_view, name='browseExcel'),
    path('auoraInfo/', auora_view, name='auoraInfo'),

    path('excelPreview/', preview_view, name='excelPreview'),

    path('api/excel/', get_excel_data, name='get_excel_data'),

    path('eventLog/', event_log, name='eventLogName'),
    path('otherEntities/', otherEntities, name='otherEntitiesName'),
    path('entityRel/', entityRel, name='entityRelName'),
    path('activityProperties/', activityProperties, name='activityPropertiesName'),
    path('Domain/', Domain, name='DomainName'),
    path('ICD/', ICD, name='ICDName'),
    path('SctNode/', SctNode, name='SctNodeName'),
    path('SctRel/', SctRel, name='SctRelName'),
    path('DK1/', DK1, name='DK1Name'),
    path('DK2/', DK2, name='DK2Name'),
    path('DK3/', DK3, name='DK3Name'),
    path('DK4/', DK4, name='DK4Name'),
    path('DK5/', DK5, name='DK5Name'),
    path('DK61/', DK61, name='DK61Name'),
    path('DK62/', DK62, name='DK62Name'),
    path('DK7/', DK7, name='DK7Name'),

    path('csvDownloading/', downloadingCsv, name='downloadingCsvName'),

    path('csvLinking/', csvLinking, name='csvLinkingName'),

###########################################
    path('conv_EvnetLog/', conv_EvnetLog, name='conv_EvnetLogName'),
    path('eventLogNeo4j/', eventLogNeo4jFunc, name='eventLogNeo4jName'),

    path('conv_otherEntities/', conv_otherEntities, name='conv_otherEntitiesName'),
    path('otherEntitiesNeo4j/', otherEntitiesNeo4jFunc, name='otherEntitiesNeo4jName'),

    path('conv_entityRel/', conv_entityRel, name='conv_entityRelName'),
    path('entityRelNeo4j/', entityRelNeo4jFunc, name='entityRelNeo4jName'),

    path('conv_activityProperties/', conv_activityProperties, name='conv_activityPropertiesName'),
    path('activityPropertiesNeo4j/', activityPropertiesNeo4jFunc, name='activityPropertiesNeo4jName'),

    path('conv_Domain/', conv_Domain, name='conv_DomainName'),
    path('DomainNeo4j/', DomainNeo4jFunc, name='DomainNeo4jName'),

    path('conv_ICD/', conv_ICD, name='conv_ICDName'),
    path('ICDNeo4j/', ICDNeo4jFunc, name='ICDNeo4jName'),

    path('conv_SctNode/', conv_SctNode, name='conv_SctNodeName'),
    path('SctNodeNeo4j/', SctNodeNeo4jFunc, name='SctNodeNeo4jName'),

    path('conv_SctRel/', conv_SctRel, name='conv_SctRelName'),
    path('SctRelNeo4j/', SctRelNeo4jFunc, name='SctRelNeo4jName'),

    path('conv_DK1/', conv_DK1, name='conv_DK1Name'),
    path('DK1Neo4j/', DK1Neo4jFunc, name='DK1Neo4jName'),

    path('conv_DK2/', conv_DK2, name='conv_DK2Name'),
    path('DK2Neo4j/', DK2Neo4jFunc, name='DK2Neo4jName'),

    path('conv_DK3/', conv_DK3, name='conv_DK3Name'),
    path('DK3Neo4j/', DK3Neo4jFunc, name='DK3Neo4jName'),

    path('conv_DK4/', conv_DK4, name='conv_DK4Name'),
    path('DK4Neo4j/', DK4Neo4jFunc, name='DK4Neo4jName'),

    path('conv_DK5/', conv_DK5, name='conv_DK5Name'),
    path('DK5Neo4j/', DK5Neo4jFunc, name='DK5Neo4jName'),

    path('conv_DK6/', conv_DK6, name='conv_DK6Name'),
    path('DK6Neo4j/', DK6Neo4jFunc, name='DK6Neo4jName'),

    path('conv_DK7/', conv_DK7, name='conv_DK7Name'),
    path('DK7Neo4j/', DK7Neo4jFunc, name='DK7Neo4jName'),

    path('conv_BuildingQuery/', conv_BuildingQuery, name='conv_BuildingQueryName'),
    path('queryLister/', queryLister, name='queryLister'),

    path('conv_DFG/', conv_DFG, name='conv_DFGName'),
    path('DFG1/', DFG, name='DFG1'),

#################################################################################

    path('convertingNeo4jCKEG1/', seve_jpegCKEG1, name='seve_jpegCKEG_name1'),
    path('convertingNeo4jCKEG2/', seve_jpegCKEG2, name='seve_jpegCKEG_name2'),
    path('convertingNeo4jCKEG3/', seve_jpegCKEG3, name='seve_jpegCKEG_name3'),
    path('convertingNeo4jCKEG4/', seve_jpegCKEG4, name='seve_jpegCKEG_name4'),
    path('convertingNeo4jCKEG5/', seve_jpegCKEG5, name='seve_jpegCKEG_name5'),
    path('convertingNeo4jCKEG6/', seve_jpegCKEG6, name='seve_jpegCKEG_name6'),
    path('convertingNeo4jCKEG7/', seve_jpegCKEG7, name='seve_jpegCKEG_name7'),
    path('convertingNeo4jCKEG8/', seve_jpegCKEG8, name='seve_jpegCKEG_name8'),
    path('convertingNeo4jCKEG9/', seve_jpegCKEG9, name='seve_jpegCKEG_name9'),
    path('convertingNeo4jCKEG10/', seve_jpegCKEG10, name='seve_jpegCKEG_name10'),
    path('convertingNeo4jCKEG11/', seve_jpegCKEG11, name='seve_jpegCKEG_name11'),
    path('convertingNeo4jCKEG12/', seve_jpegCKEG12, name='seve_jpegCKEG_name12'),
    path('convertingNeo4jCKEG13/', seve_jpegCKEG13, name='seve_jpegCKEG_name13'),
    path('convertingNeo4jCKEG14/', seve_jpegCKEG14, name='seve_jpegCKEG_name14'),
    path('convertingNeo4jCKEG15/', seve_jpegCKEG15, name='seve_jpegCKEG_name15'),
    path('convertingNeo4jCKEG16/', seve_jpegCKEG16, name='seve_jpegCKEG_name16'),
    path('convertingNeo4jCKEG17/', seve_jpegCKEG17, name='seve_jpegCKEG_name17'),



    path('eventLogNeo4jQ1/',  seve_neo4jQuery_funcQ1_EventLog, name='seve_neo4jQuery_nameQ1_EventLog'),
    path('eventLogNeo4jQ2/',  seve_neo4jQuery_funcQ2_EventLog, name='seve_neo4jQuery_nameQ2_EventLog'),
    path('eventLogNeo4jQ3/',  seve_neo4jQuery_funcQ3_EventLog, name='seve_neo4jQuery_nameQ3_EventLog'),
    path('eventLogNeo4jQ4/',  seve_neo4jQuery_funcQ4_EventLog, name='seve_neo4jQuery_nameQ4_EventLog'),
    path('eventLogNeo4jQ5/',  seve_neo4jQuery_funcQ5_EventLog, name='seve_neo4jQuery_nameQ5_EventLog'),
    path('eventLogNeo4jQ6/',  seve_neo4jQuery_funcQ6_EventLog, name='seve_neo4jQuery_nameQ6_EventLog'),
    path('eventLogNeo4jQ7/',  seve_neo4jQuery_funcQ7_EventLog, name='seve_neo4jQuery_nameQ7_EventLog'),
    path('eventLogNeo4jQ8/',  seve_neo4jQuery_funcQ8_EventLog, name='seve_neo4jQuery_nameQ8_EventLog'),
    path('eventLogNeo4jQ9/',  seve_neo4jQuery_funcQ9_EventLog, name='seve_neo4jQuery_nameQ9_EventLog'),
    path('eventLogNeo4jQ10/',  seve_neo4jQuery_funcQ10_EventLog, name='seve_neo4jQuery_nameQ10_EventLog'),
    path('eventLogNeo4jQ11/',  seve_neo4jQuery_funcQ11_EventLog, name='seve_neo4jQuery_nameQ11_EventLog'),
    path('eventLogNeo4jQ12/',  seve_neo4jQuery_funcQ12_EventLog, name='seve_neo4jQuery_nameQ12_EventLog'),
    path('otherEntitiesNeo4jQ1/',  seve_neo4jQuery_funcQ1_otherEntities, name='seve_neo4jQuery_nameQ1_otherEntities'),
    path('otherEntitiesNeo4jQ2/',  seve_neo4jQuery_funcQ2_otherEntities, name='seve_neo4jQuery_nameQ2_otherEntities'),
    path('otherEntitiesNeo4jQ3/',  seve_neo4jQuery_funcQ3_otherEntities, name='seve_neo4jQuery_nameQ3_otherEntities'),
    path('otherEntitiesNeo4jQ4/',  seve_neo4jQuery_funcQ4_otherEntities, name='seve_neo4jQuery_nameQ4_otherEntities'),
    path('entityRelNeo4jQ1/',  seve_neo4jQuery_funcQ1_entityRel, name='seve_neo4jQuery_nameQ1_entityRel'),
    path('entityRelNeo4jQ2/',  seve_neo4jQuery_funcQ2_entityRel, name='seve_neo4jQuery_nameQ2_entityRel'),
    path('entityRelNeo4jQ3/',  seve_neo4jQuery_funcQ3_entityRel, name='seve_neo4jQuery_nameQ3_entityRel'),
    path('entityRelNeo4jQ4/',  seve_neo4jQuery_funcQ4_entityRel, name='seve_neo4jQuery_nameQ4_entityRel'),
    path('entityRelNeo4jQ5/',  seve_neo4jQuery_funcQ5_entityRel, name='seve_neo4jQuery_nameQ5_entityRel'),
    path('entityRelNeo4jQ6/',  seve_neo4jQuery_funcQ6_entityRel, name='seve_neo4jQuery_nameQ6_entityRel'),
    path('entityRelNeo4jQ7/',  seve_neo4jQuery_funcQ7_entityRel, name='seve_neo4jQuery_nameQ7_entityRel'),
    path('entityRelNeo4jQ8/',  seve_neo4jQuery_funcQ8_entityRel, name='seve_neo4jQuery_nameQ8_entityRel'),
    path('entityRelNeo4jQ9/',  seve_neo4jQuery_funcQ9_entityRel, name='seve_neo4jQuery_nameQ9_entityRel'),
    path('entityRelNeo4jQ10/',  seve_neo4jQuery_funcQ10_entityRel, name='seve_neo4jQuery_nameQ10_entityRel'),
    path('entityRelNeo4jQ11/',  seve_neo4jQuery_funcQ11_entityRel, name='seve_neo4jQuery_nameQ11_entityRel'),
    path('entityRelNeo4jQ12/',  seve_neo4jQuery_funcQ12_entityRel, name='seve_neo4jQuery_nameQ12_entityRel'),
    path('activityPropertiesNeo4jQ1/',  seve_neo4jQuery_funcQ1_activityProperties, name='seve_neo4jQuery_nameQ1_activityProperties'),
    path('activityPropertiesNeo4jQ2/',  seve_neo4jQuery_funcQ2_activityProperties, name='seve_neo4jQuery_nameQ2_activityProperties'),
    path('activityPropertiesNeo4jQ3/',  seve_neo4jQuery_funcQ3_activityProperties, name='seve_neo4jQuery_nameQ3_activityProperties'),
    path('activityPropertiesNeo4jQ4/',  seve_neo4jQuery_funcQ4_activityProperties, name='seve_neo4jQuery_nameQ4_activityProperties'),
    path('activityPropertiesNeo4jQ5/',  seve_neo4jQuery_funcQ5_activityProperties, name='seve_neo4jQuery_nameQ5_activityProperties'),
    path('DomainNeo4jQ1/',  seve_neo4jQuery_funcQ1_Domain, name='seve_neo4jQuery_nameQ1_Domain'),
    path('DomainNeo4jQ2/',  seve_neo4jQuery_funcQ2_Domain, name='seve_neo4jQuery_nameQ2_Domain'),
    path('DomainNeo4jQ3/',  seve_neo4jQuery_funcQ3_Domain, name='seve_neo4jQuery_nameQ3_Domain'),
    path('DomainNeo4jQ4/',  seve_neo4jQuery_funcQ4_Domain, name='seve_neo4jQuery_nameQ4_Domain'),
    path('ICDNeo4jQ1/',  seve_neo4jQuery_funcQ1_ICD, name='seve_neo4jQuery_nameQ1_ICD'),
    path('ICDNeo4jQ2/',  seve_neo4jQuery_funcQ2_ICD, name='seve_neo4jQuery_nameQ2_ICD'),
    path('ICDNeo4jQ3/',  seve_neo4jQuery_funcQ3_ICD, name='seve_neo4jQuery_nameQ3_ICD'),
    path('ICDNeo4jQ4/',  seve_neo4jQuery_funcQ4_ICD, name='seve_neo4jQuery_nameQ4_ICD'),
    path('SctNodeNeo4jQ1/',  seve_neo4jQuery_funcQ1_sctNode, name='seve_neo4jQuery_nameQ1_sctNode'),
    path('SctNodeNeo4jQ2/',  seve_neo4jQuery_funcQ2_sctNode, name='seve_neo4jQuery_nameQ2_sctNode'),
    path('SctNodeNeo4jQ3/',  seve_neo4jQuery_funcQ3_sctNode, name='seve_neo4jQuery_nameQ3_sctNode'),
    path('SctNodeNeo4jQ4/',  seve_neo4jQuery_funcQ4_sctNode, name='seve_neo4jQuery_nameQ4_sctNode'),
    path('SctRelNeo4jQ1/',  seve_neo4jQuery_funcQ1_sctRel, name='seve_neo4jQuery_nameQ1_sctRel'),
    path('SctRelNeo4jQ2/',  seve_neo4jQuery_funcQ2_sctRel, name='seve_neo4jQuery_nameQ2_sctRel'),
    path('SctRelNeo4jQ3/',  seve_neo4jQuery_funcQ3_sctRel, name='seve_neo4jQuery_nameQ3_sctRel'),
    path('DK3Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK3, name='seve_neo4jQuery_nameQ1_DK3'),
    path('DK3Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK3, name='seve_neo4jQuery_nameQ2_DK3'),
    path('DK4Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK4, name='seve_neo4jQuery_nameQ1_DK4'),
    path('DK4Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK4, name='seve_neo4jQuery_nameQ2_DK4'),
    path('DK5Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK5, name='seve_neo4jQuery_nameQ1_DK5'),
    path('DK5Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK5, name='seve_neo4jQuery_nameQ2_DK5'),
    path('DK5Neo4jQ3/',  seve_neo4jQuery_funcQ3_DK5, name='seve_neo4jQuery_nameQ3_DK5'),
    path('DK6Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK6, name='seve_neo4jQuery_nameQ1_DK6'),
    path('DK6Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK6, name='seve_neo4jQuery_nameQ2_DK6'),
    path('DK7Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK7, name='seve_neo4jQuery_nameQ1_DK7'),
    path('DK7Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK7, name='seve_neo4jQuery_nameQ2_DK7'),
    path('eventLogNeo4jQ4svg/', seve_neo4jQuery_svgQ4_EventLog, name='seve_neo4jQuery_svg_nameQ4_EventLog'),
    path('eventLogNeo4jQ5svg/', seve_neo4jQuery_svgQ5_EventLog, name='seve_neo4jQuery_svg_nameQ5_EventLog'),
    path('eventLogNeo4jQ6svg/', seve_neo4jQuery_svgQ6_EventLog, name='seve_neo4jQuery_svg_nameQ6_EventLog'),
    path('eventLogNeo4jQ7svg/', seve_neo4jQuery_svgQ7_EventLog, name='seve_neo4jQuery_svg_nameQ7_EventLog'),
    path('eventLogNeo4jQ8svg/', seve_neo4jQuery_svgQ8_EventLog, name='seve_neo4jQuery_svg_nameQ8_EventLog'),
    path('eventLogNeo4jQ9svg/', seve_neo4jQuery_svgQ9_EventLog, name='seve_neo4jQuery_svg_nameQ9_EventLog'),
    path('eventLogNeo4jQ10svg/', seve_neo4jQuery_svgQ10_EventLog, name='seve_neo4jQuery_svg_nameQ10_EventLog'),
    path('eventLogNeo4jQ11svg/', seve_neo4jQuery_svgQ11_EventLog, name='seve_neo4jQuery_svg_nameQ11_EventLog'),
    path('eventLogNeo4jQ12svg/', seve_neo4jQuery_svgQ12_EventLog, name='seve_neo4jQuery_svg_nameQ12_EventLog'),
    path('otherEntitiesNeo4jQ1svg/', seve_neo4jQuery_svgQ4_otherEntities,
         name='seve_neo4jQuery_svg_nameQ4_otherEntities'),
    path('entityRelNeo4jQ1svg/', seve_neo4jQuery_svgQ3_entityRel, name='seve_neo4jQuery_svg_nameQ3_entityRel'),
    path('entityRelNeo4jQ2svg/', seve_neo4jQuery_svgQ6_entityRel, name='seve_neo4jQuery_svg_nameQ6_entityRel'),
    path('entityRelNeo4jQ3svg/', seve_neo4jQuery_svgQ7_entityRel, name='seve_neo4jQuery_svg_nameQ7_entityRel'),
    path('entityRelNeo4jQ4svg/', seve_neo4jQuery_svgQ8_entityRel, name='seve_neo4jQuery_svg_nameQ8_entityRel'),
    path('entityRelNeo4jQ5svg/', seve_neo4jQuery_svgQ9_entityRel, name='seve_neo4jQuery_svg_nameQ9_entityRel'),
    path('entityRelNeo4jQ6svg/', seve_neo4jQuery_svgQ10_entityRel, name='seve_neo4jQuery_svg_nameQ10_entityRel'),
    path('entityRelNeo4jQ7svg/', seve_neo4jQuery_svgQ11_entityRel, name='seve_neo4jQuery_svg_nameQ11_entityRel'),
    path('entityRelNeo4jQ8svg/', seve_neo4jQuery_svgQ12_entityRel, name='seve_neo4jQuery_svg_nameQ12_entityRel'),
    path('activityPropertiesNeo4jQ1svg/', seve_neo4jQuery_svgQ4_activityProperties,
         name='seve_neo4jQuery_svg_nameQ4_activityProperties'),
    path('activityPropertiesNeo4jQ2svg/', seve_neo4jQuery_svgQ5_activityProperties,
         name='seve_neo4jQuery_svg_nameQ5_activityProperties'),
    path('DomainNeo4jQ4svg/', seve_neo4jQuery_svgQ4_Domain, name='seve_neo4jQuery_svg_nameQ4_Domain'),
    path('ICDNeo4jQ4svg/', seve_neo4jQuery_svgQ4_ICD, name='seve_neo4jQuery_svg_nameQ4_ICD'),
    path('SctNodeNeo4jQ1svg/', seve_neo4jQuery_svgQ4_sctNode, name='seve_neo4jQuery_svg_nameQ4_sctNode'),
    path('SctRelNeo4jQ1svg/', seve_neo4jQuery_svgQ2_sctRel, name='seve_neo4jQuery_svg_nameQ2_sctRel'),
    path('SctRelNeo4jQ2svg/', seve_neo4jQuery_svgQ3_sctRel, name='seve_neo4jQuery_svg_nameQ3_sctRel'),
    path('DK3Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK3, name='seve_neo4jQuery_svg_nameQ2_DK3'),
    path('DK4Neo4jQ2svg/', seve_neo4jQuery_svgQ2_DK4, name='seve_neo4jQuery_svg_nameQ2_DK4'),
    path('DK5Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK5, name='seve_neo4jQuery_svg_nameQ2_DK5'),
    path('DK5Neo4jQ2svg/', seve_neo4jQuery_svgQ3_DK5, name='seve_neo4jQuery_svg_nameQ3_DK5'),
    path('DK6Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK6, name='seve_neo4jQuery_svg_nameQ2_DK6'),
    path('DK7Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK7, name='seve_neo4jQuery_svg_nameQ2_DK7'),



    path('queryListerQ1/',  seve_neo4jQuery_funcQ1_Final, name='seve_neo4jQuery_nameQ1_Final'),
    path('queryListerQ2/',  seve_neo4jQuery_funcQ2_Final, name='seve_neo4jQuery_nameQ2_Final'),
    path('queryListerQ3/',  seve_neo4jQuery_funcQ3_Final, name='seve_neo4jQuery_nameQ3_Final'),
    path('queryListerQ4/',  seve_neo4jQuery_funcQ4_Final, name='seve_neo4jQuery_nameQ4_Final'),
    path('queryListerQ5/',  seve_neo4jQuery_funcQ5_Final, name='seve_neo4jQuery_nameQ5_Final'),
    path('queryListerQ6/',  seve_neo4jQuery_funcQ6_Final, name='seve_neo4jQuery_nameQ6_Final'),
    path('queryListerQ7/',  seve_neo4jQuery_funcQ7_Final, name='seve_neo4jQuery_nameQ7_Final'),
    path('queryListerQ8/',  seve_neo4jQuery_funcQ8_Final, name='seve_neo4jQuery_nameQ8_Final'),
    path('queryListerQ9/',  seve_neo4jQuery_funcQ9_Final, name='seve_neo4jQuery_nameQ9_Final'),
    path('queryListerQ10/',  seve_neo4jQuery_funcQ10_Final, name='seve_neo4jQuery_nameQ10_Final'),
    path('queryListerQ11/',  seve_neo4jQuery_funcQ11_Final, name='seve_neo4jQuery_nameQ11_Final'),
    path('queryListerQ12/',  seve_neo4jQuery_funcQ12_Final, name='seve_neo4jQuery_nameQ12_Final'),
    path('queryListerQ13/',  seve_neo4jQuery_funcQ13_Final, name='seve_neo4jQuery_nameQ13_Final'),
    path('queryListerQ14/',  seve_neo4jQuery_funcQ14_Final, name='seve_neo4jQuery_nameQ14_Final'),
    path('queryListerQ15/',  seve_neo4jQuery_funcQ15_Final, name='seve_neo4jQuery_nameQ15_Final'),
    path('queryListerQ16/',  seve_neo4jQuery_funcQ16_Final, name='seve_neo4jQuery_nameQ16_Final'),
    path('queryListerQ17/',  seve_neo4jQuery_funcQ17_Final, name='seve_neo4jQuery_nameQ17_Final'),
    path('queryListerQ18/',  seve_neo4jQuery_funcQ18_Final, name='seve_neo4jQuery_nameQ18_Final'),
    path('queryListerQ19/', seve_neo4jQuery_funcQ19_Final, name='seve_neo4jQuery_nameQ19_Final'),
    path('queryListerQ20/', seve_neo4jQuery_funcQ20_Final, name='seve_neo4jQuery_nameQ20_Final'),
    path('queryListerQ21/', seve_neo4jQuery_funcQ21_Final, name='seve_neo4jQuery_nameQ21_Final'),
    path('queryListerQ22/', seve_neo4jQuery_funcQ22_Final, name='seve_neo4jQuery_nameQ22_Final'),
    path('queryListerQ3svg/', seve_neo4jQuery_svgQ3_Final, name='seve_neo4jQuery_svg_nameQ3_Final'),
    path('queryListerQ4svg/', seve_neo4jQuery_svgQ4_Final, name='seve_neo4jQuery_svg_nameQ4_Final'),
    path('queryListerQ5svg/', seve_neo4jQuery_svgQ5_Final, name='seve_neo4jQuery_svg_nameQ5_Final'),
    path('queryListerQ6svg/', seve_neo4jQuery_svgQ6_Final, name='seve_neo4jQuery_svg_nameQ6_Final'),
    path('queryListerQ7svg/', seve_neo4jQuery_svgQ7_Final, name='seve_neo4jQuery_svg_nameQ7_Final'),
    path('queryListerQ8svg/', seve_neo4jQuery_svgQ8_Final, name='seve_neo4jQuery_svg_nameQ8_Final'),
    path('queryListerQ9svg/', seve_neo4jQuery_svgQ9_Final, name='seve_neo4jQuery_svg_nameQ9_Final'),
    path('queryListerQ10svg/', seve_neo4jQuery_svgQ10_Final, name='seve_neo4jQuery_svg_nameQ10_Final'),
    path('queryListerQ11svg/', seve_neo4jQuery_svgQ11_Final, name='seve_neo4jQuery_svg_nameQ11_Final'),
    path('queryListerQ12svg/', seve_neo4jQuery_svgQ12_Final, name='seve_neo4jQuery_svg_nameQ12_Final'),
    path('queryListerQ13svg/', seve_neo4jQuery_svgQ13_Final, name='seve_neo4jQuery_svg_nameQ13_Final'),
    path('queryListerQ14svg/', seve_neo4jQuery_svgQ14_Final, name='seve_neo4jQuery_svg_nameQ14_Final'),
    path('queryListerQ15svg/', seve_neo4jQuery_svgQ15_Final, name='seve_neo4jQuery_svg_nameQ15_Final'),
    path('queryListerQ16svg/', seve_neo4jQuery_svgQ16_Final, name='seve_neo4jQuery_svg_nameQ16_Final'),
    path('queryListerQ17svg/', seve_neo4jQuery_svgQ17_Final, name='seve_neo4jQuery_svg_nameQ17_Final'),
    path('queryListerQ18svg/', seve_neo4jQuery_svgQ18_Final, name='seve_neo4jQuery_svg_nameQ18_Final'),
    path('queryListerQ19svg/', seve_neo4jQuery_svgQ19_Final, name='seve_neo4jQuery_svg_nameQ19_Final'),
    path('queryListerQ20svg/', seve_neo4jQuery_svgQ20_Final, name='seve_neo4jQuery_svg_nameQ20_Final'),
    path('queryListerQ21svg/', seve_neo4jQuery_svgQ21_Final, name='seve_neo4jQuery_svg_nameQ21_Final'),
    path('queryListerQ22svg/', seve_neo4jQuery_svgQ22_Final, name='seve_neo4jQuery_svg_nameQ22_Final'),




    path('serve-pdf/', serve_pdf_func, name='serve_pdf_name'),
    path('serve-dot/', serve_dot_func, name='serve_dot_name'),
    path('serve-graphvizQ/', serve_graphvizQuery_func, name='serve_graphvizQ_name'),
    path('serve-neo4jQ/', serve_neo4jQuery_func, name='serve_neo4jQ_name'),



]
