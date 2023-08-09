from dataclasses import dataclass

@dataclass
class NameContent:
    order: int
    name: str
    content: str

    def __init__(self, order, name, content):
        self.order = order
        self.name = name
        self.content = content

@dataclass
class NameContentType:
    order: int
    name: str
    type: str
    content: str

    def __init__(self, order, name, type, content):
        self.order = order
        self.name = name
        self.type = type
        self.content = content

@dataclass
class VqlBaseView(NameContentType):
    wrapper: str

    def __init__(self, order, name, type, wrapper, content):
        super().__init__(order, name, type, content)
        self.wrapper = wrapper

@dataclass
class VqlView(NameContent):
    has_datamovement: bool
    is_consumption: bool
    is_remote_table: bool

    def __init__(self, order, name, has_dt, is_consumption, is_remote, content):
        super().__init__(order, name, content)
        self.has_datamovement = has_dt
        self.is_consumption = is_consumption
        self.is_remote_table = is_remote

@dataclass
class VqlFolder(NameContent):
    pass

@dataclass
class VqlUser(NameContent):
  pass

@dataclass
class VqlRole(NameContent):
  pass

@dataclass
class VqlDatasource(NameContentType):
  pass

@dataclass
class VqlWrapper(NameContentType):
  pass

@dataclass
class VqlDatabase(NameContent):
  pass

@dataclass
class VqlListener(NameContentType):
  pass

@dataclass
class VqlProcedure(NameContentType):
  pass

@dataclass
class VqlType(NameContent):
  pass

@dataclass
class VqlMap(NameContentType):
  pass

@dataclass
class VqlInterfaceView(NameContent):
  pass

@dataclass
class VqlAssociation(NameContent):
  pass

@dataclass
class VqlWidget(NameContent):
  pass

@dataclass
class VqlService(NameContent):
  pass