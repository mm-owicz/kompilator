from enum import Enum


class Value:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class VarType(Enum):
    INT32 = 1
    INT64 = 2
    FLOAT32 = 3
    FLOAT64 = 4
    BOOL = 5
    STRING = 6
    ARRAY = 7
    STRUCT = 8

def string_to_type(string):
    if string == "int32":
        return VarType.INT32
    elif string == "int64":
        return VarType.INT64
    elif string == "float32":
        return VarType.FLOAT32
    elif string == "float64":
        return VarType.FLOAT64
    elif string == 'bool' or string == VarType.BOOL:
        return VarType.BOOL
    elif string == 'str':
        return VarType.STRING
    else:
       return string

def type_to_string(var_type):
    if var_type == VarType.INT32:
        return "int32"
    elif var_type == VarType.INT64:
        return "int64"
    elif var_type == VarType.FLOAT32:
       return "float32"
    elif var_type == VarType.FLOAT64:
        return "float64"
    elif var_type == VarType.BOOL:
        return "i1"
    elif var_type == VarType.STRING:
        return "i8"
    else:
       raise Exception(f"Unsuported type - {var_type}")

def get_llvm_type_str(varTp):
    if varTp == VarType.INT32:
        return 'i32'
    elif varTp == VarType.INT64:
        return 'i64'
    elif varTp == VarType.FLOAT32:
        return 'float'
    elif varTp == VarType.FLOAT64:
        return 'double'
    elif varTp == VarType.BOOL:
        return 'i1'
    elif varTp == VarType.STRING:
        return 'i8*'
    # elif varTp == VarType.ARRAY:
    #     return ''

def llvm_to_type(varTp):
    if varTp == 'i32':
        return VarType.INT32
    elif varTp == 'i64':
        return VarType.INT64
    elif varTp == 'float':
        return VarType.FLOAT32
    elif varTp == 'double':
        return VarType.FLOAT64
    elif varTp == 'i1':
        return VarType.BOOL
    elif varTp == 'i8*':
        return VarType.STRING
    # elif varTp == VarType.ARRAY:
    #     return ''
