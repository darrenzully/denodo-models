from __future__ import annotations
from typing import List
from dataclasses import dataclass, field

from vqlElements import VqlAssociation, VqlView, VqlBaseView, VqlDatabase, VqlDatasource, VqlFolder, VqlInterfaceView, VqlListener, VqlMap, VqlProcedure, VqlRole, VqlService, VqlType, VqlUser, VqlWidget, VqlWrapper

@dataclass
class VqlFile:
   database: str
   create_users: List[VqlUser] = field(default_factory=[])
   create_roles: List[VqlRole] = field(default_factory=[])
   create_database: VqlDatabase = field(default_factory=VqlDatabase)
   create_folders: List[VqlFolder] = field(default_factory=[])
   create_listeners: List[VqlListener] = field(default_factory=[])
   create_datasources: List[VqlDatasource] = field(default_factory=[])
   alter_database: List[VqlDatabase] = field(default_factory=[])
   create_wrappers: List[VqlWrapper] = field(default_factory=[])
   create_procedures: List[VqlProcedure] = field(default_factory=[])
   create_types: List[VqlType] = field(default_factory=[])
   create_maps: List[VqlMap] = field(default_factory=[])
   create_base_views: List[VqlBaseView] = field(default_factory=[])
   create_views: List[VqlView] = field(default_factory=[])
   create_interfaces: List[VqlInterfaceView] = field(default_factory=[])
   create_associations: List[VqlAssociation] = field(default_factory=[])
   create_services: List[VqlService] = field(default_factory=[])
   create_widgets: List[VqlWidget] = field(default_factory=[])
   deploy_services: List[VqlService] = field(default_factory=[])
   deploy_widgets: List[VqlWidget] = field(default_factory=[])
   undeploy_services: List[VqlService] = field(default_factory=[])
   undeploy_widgets: List[VqlWidget] = field(default_factory=[])
   alter_users: List[VqlUser] = field(default_factory=[])
   alter_roles: List[VqlRole] = field(default_factory=[])
   
   def get_base_views(self) -> List:
      return [(bv.name, bv.type) for bv in self.create_base_views]

   def get_derived_views(self) -> List:
      return [dv.name for dv in self.create_views]

   def get_interfaces(self) -> List:
      return [i.name for i in self.create_interfaces]
    
   def get_wrappers(self) -> List:
      return [(wr.name, wr.type) for wr in self.create_wrappers]
    
   def __init__(self, name=None):
      self.database = name if name else ""
      self.create_users = []
      self.create_roles = []
      self.create_database = None
      self.create_folders = []
      self.create_listeners = []
      self.create_datasources = []
      self.alter_database = []
      self.create_wrappers = []
      self.create_procedures = []
      self.create_types = []
      self.create_maps = []
      self.create_base_views = []
      self.create_views = []
      self.create_interfaces = []
      self.create_associations = []
      self.create_services = []
      self.create_widgets = []
      self.deploy_services = []
      self.deploy_widgets = []
      self.undeploy_services = []
      self.undeploy_widgets = []
      self.alter_users = []
      self.alter_roles = []

   def __str__(self):
      return f'VqlFile for database: {self.database}'


   def __repr__(self):
      return self.__str__()


