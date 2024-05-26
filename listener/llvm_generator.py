from listener.value import VarType, Value, get_llvm_type_str, llvm_to_type

class LLVMGenerator():

    def __init__(self):
        self.reg = 1
        self.mreg = 1
        self.br = 0
        self.br_stack = []
        self.label_count = 0
        self.code_text = ""
        self.symbol_table = {}
        self.result_code = ""
        self.header_text = ""
        self.str = 1
        # self.header_text += f"@str_ptr = global [2 x i8]\n"
        # self.header_text += f"store [2 x i8] c\"\\0A\\00\", [2 x i8]* @str_ptr\n"
        self.header_text += f"@str_ptr = constant [2 x i8]c\"\\0A\\00\" \n"

    
    def element_assign(self, ident, indx, value, type, size):
        self.code_text += f"%{self.reg} = getelementptr inbounds[{size} x {type}], ptr {ident}, i64 0, i64 {indx}\n"
        self.code_text += f"store {type} {value}, ptr %{self.reg}\n"
        self.reg += 1

    def array_access(self, ident, indx, type, size):
        self.code_text += f"%{self.reg} = getelementptr inbounds[{size} x {type}], ptr {ident}, i64 0, i64 {indx}\n"
        self.reg += 1
        self.code_text += f"%{self.reg} = load {type}, {type}* %{self.reg - 1}\n"
        self.reg += 1
        
    def declare_array(self, ident, type, size, global_arr):
        if global_arr:
            ident = ident.replace("%", "@") if "%" in ident else ident
            self.header_text += '@' + str(ident) + f" = global [{size} x {type}] zeroinitializer\n"
        else:
            self.code_text += f"%{ident} = alloca [{size} x {type}]\n"

    def assign_array(self, ident, type, size, values):
        for i in range(len(values)):
            self.element_assign(ident, i, values[i], type, size)


    def assign_struct(self, ident, structID, is_global):
        if is_global:
            self.header_text += f"{ident} = global %{structID} zeroinitializer\n"
        else:
            self.code_text += f"{ident} = alloca %{structID}\n"

    def assign_struct_member(self, ident, name, index, value, type):
        self.code_text += f"%{self.reg} = getelementptr %{name}, %{name}* {ident}, i32 0, i32 {index}\n"
        self.code_text += f"store {type} {value}, {type}* %{self.reg}\n"
        self.reg += 1

    def struct_access(self, ident, name, index, type):
        self.code_text += f"%{self.reg} = getelementptr %{name}, %{name}* {ident}, i32 0, i32 {index}\n"
        self.reg += 1
        self.code_text += f"%{self.reg} = load {type}, {type}* %{self.reg - 1}\n"
        self.reg += 1

    def declare_struct(self, ident, vars):
        self.header_text += f"%{ident} = type " + '{'
        for index, v in enumerate(vars):
            if index == len(vars) - 1:
                self.header_text += f"{v.type}"
            else:
                self.header_text += f"{v.type}, "
        self.header_text += "}\n"

    def store_var_bool_op(self, var, sym):
        try:
            self.code_text += '%' + str(self.reg) + ' = alloca i1\n'
            self.reg += 1
            if var.name == 'true':
                self.code_text += "store i1 1, i1* %" + str(self.reg) + "\n"
            elif var.name == 'false':
                self.code_text += "store i1 0, i1* %" + str(self.reg) + "\n"
            else:
                self.code_text += "store i1 " + var.name + ", i1* %" + str(self.reg) + '\n'
            var = str(self.reg)
            self.reg += 1
        except Exception as e:
            pass
        self.code_text += "%" + str(self.reg) + " = load i1, i1* " + sym + var + "\n"
        self.reg += 1
        return var

    def or_operation(self, left, right, sym1, sym2):
        evalSecondLabel = f"evalSecond{self.label_count}"
        endLabel = f"endLogicalOr{self.label_count}"
        finalFalse = f"finalFalse{self.label_count}"
        finalTrue = f"finalTrue{self.label_count}"
        self.label_count += 1

        left = self.store_var_bool_op(left, sym1)

        # short cirtuit boolean operation:
        self.code_text += f"br i1 %{str(self.reg - 1)}, label %{finalTrue}, label %{evalSecondLabel}\n"

        self.code_text += f"{evalSecondLabel}:\n"
        right = self.store_var_bool_op(right, sym2)

        self.code_text += f'br i1 %{str(self.reg - 1)}, label %{finalTrue}, label %{finalFalse}\n'
        self.code_text += f"{finalTrue}:\n"
        self.code_text += f"br label %{endLabel}\n"
        self.code_text += f"{finalFalse}:\n"
        self.code_text += f"br label %{endLabel}\n"
        self.code_text += f"{endLabel}:\n"
        resultReg = self.reg
        self.reg += 1
        self.code_text += f"%{resultReg} = phi i1 [1, %{finalTrue}], [0, %{finalFalse}]\n"

    def neg_operation(self, factor):
        # right = Value('true', 3)
        
        # left = self.store_var_bool_op(left)
        # right = self.store_var_bool_op(right)


        # left = str(self.reg - 4)
        # right = str(self.reg - 1)
        # self.code_text += "%" + str(self.reg) + " = xor i1 %" + left + ", %" + right + "\n"
        # self.reg += 1
        pass


    def xor_operation(self, left, right, sym1, sym2):
        left = self.store_var_bool_op(left, sym1)
        right = self.store_var_bool_op(right, sym2)
        left = str(self.reg - 3)
        right = str(self.reg - 1)
        self.code_text += "%" + str(self.reg) + " = xor i1 %" + left + ", %" + right + "\n"
        self.reg += 1
    
    def and_operation(self, left, right, sym1, sym2):
        evalSecondLabel = f"evalSecond{self.label_count}"
        endLabel = f"endLogicalAnd{self.label_count}"
        finalFalse = f"finalFalse{self.label_count}"
        finalTrue = f"finalTrue{self.label_count}"
        self.label_count += 1

        left = self.store_var_bool_op(left, sym1)

        # short cirtuit boolean operation:
        self.code_text += f"br i1 %{str(self.reg - 1)}, label %{evalSecondLabel}, label %{finalFalse}\n"
        
        self.code_text += f"{evalSecondLabel}:\n"
        right = self.store_var_bool_op(right, sym2)

        self.code_text += f'br i1 %{str(self.reg - 1)}, label %{finalTrue}, label %{finalFalse}\n'
        self.code_text += f"{finalTrue}:\n"
        self.code_text += f"br label %{endLabel}\n"
        self.code_text += f"{finalFalse}:\n"
        self.code_text += f"br label %{endLabel}\n"
        self.code_text += f"{endLabel}:\n"
        resultReg = self.reg
        self.reg += 1
        self.code_text += f"%{resultReg} = phi i1 [1, %{finalTrue}], [0, %{finalFalse}]\n"


    def rel_operation(self, left, right, oper, sym):
        if oper == '==': # eq
            op = "eq"
        elif oper == '!=': # ne
            op = "ne"
        elif oper == '<': # slt
            op = "slt"
        elif oper == '>': # sgt
            op = "sgt"
        elif oper == '<=': # sle
            op = "sle"
        elif oper == '>=': # sge
            op = "sge"
        
        l = self.symbol_table[left].name
        self.code_text += "%"+ str(self.reg) + " = icmp " + op + " i32 " + str(l) + ", " + str(right) + "\n"
        self.reg += 1

    def add_operation(self, left, right, operator):
        left = self.symbol_table[left]
        right = self.symbol_table[right]
        if operator == "+":            
            if left.type == VarType.INT32 and right.type == VarType.INT32 :
                self.code_text += "%" + str(self.reg) + " = add i32 " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.INT32
            elif left.type == VarType.INT64 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = add i64 " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.INT64
            elif left.type == VarType.FLOAT32 and right.type == VarType.FLOAT32:
                self.code_text += "%" + str(self.reg) + " = fadd float " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT32
            elif left.type == VarType.FLOAT64 and right.type == VarType.FLOAT64:
                self.code_text += "%" + str(self.reg) + " = fadd double " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT64


            elif left.type == VarType.INT32 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = sext i32 " + left.name + " to i64\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = add i64 " + "%" + str(self.reg - 1) + ", " + right.name + "\n"
                self.reg += 1
                return VarType.INT64

            elif left.type == VarType.INT64 and right.type == VarType.INT32:
                self.code_text += "%" + str(self.reg) + " = sext i32 " + right.name + " to i64\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = add i64 " + left.name + ", %" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.INT64



            elif left.type == VarType.INT32 and right.type == VarType.FLOAT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + left.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd float " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT32
            elif left.type == VarType.INT64 and right.type == VarType.FLOAT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + left.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd float " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT32

            elif left.type == VarType.INT32 and right.type == VarType.FLOAT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + left.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd double " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT64
            elif left.type == VarType.INT64 and right.type == VarType.FLOAT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + left.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd double " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT64

           

            elif left.type == VarType.FLOAT32 and right.type == VarType.INT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + right.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd float " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT32
            elif left.type == VarType.FLOAT32 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + right.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd float " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT32

            elif left.type == VarType.FLOAT64 and right.type == VarType.INT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + right.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd double " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT64
            elif left.type == VarType.FLOAT64 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + right.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fadd double " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT64

        elif operator == "-":
            #takie same
            if left.type == VarType.INT32 and right.type == VarType.INT32 :
                self.code_text += "%" + str(self.reg) + " = sub i32 " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.INT32
            elif left.type == VarType.INT64 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = sub i64 " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.INT64
            elif left.type == VarType.FLOAT32 and right.type == VarType.FLOAT32:
                self.code_text += "%" + str(self.reg) + " = fsub float " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT32
            elif left.type == VarType.FLOAT64 and right.type == VarType.FLOAT64:
                self.code_text += "%" + str(self.reg) + " = fsub double " + left.name + ", " + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT64

            
            
            elif left.type == VarType.INT32 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = sext i32 " + left.name + " to i64\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = sub i64 " + "%" + str(self.reg - 1) + ", " + right.name + "\n"
                self.reg += 1
                return VarType.INT64

            elif left.type == VarType.INT64 and right.type == VarType.INT32:
                self.code_text += "%" + str(self.reg) + " = sext i32 " + right.name + " to i64\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = sub i64 " + left.name + ", %" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.INT64

            elif left.type == VarType.INT32 and right.type == VarType.FLOAT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + left.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub float " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT32
            elif left.type == VarType.INT64 and right.type == VarType.FLOAT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + left.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub float " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT32

            elif left.type == VarType.INT32 and right.type == VarType.FLOAT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + left.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub double " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT64
            elif left.type == VarType.INT64 and right.type == VarType.FLOAT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + left.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub double " + "%" + str(self.reg - 1) + "," + right.name + "\n"
                self.reg += 1
                return VarType.FLOAT64

     

            elif left.type == VarType.FLOAT32 and right.type == VarType.INT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + right.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub float " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT32
            elif left.type == VarType.FLOAT32 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + right.name + " to float\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub float " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT32

            elif left.type == VarType.FLOAT64 and right.type == VarType.INT32:
                self.code_text += "%" + str(self.reg) + " = sitofp i32 " + right.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub double " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT64
            elif left.type == VarType.FLOAT64 and right.type == VarType.INT64:
                self.code_text += "%" + str(self.reg) + " = sitofp i64 " + right.name + " to double\n"
                self.reg += 1
                self.code_text += "%" + str(self.reg) + " = fsub double " + left.name + ", " + "%" + str(self.reg - 1) + "\n"
                self.reg += 1
                return VarType.FLOAT64
            

    def mult_operation(self, left, right, oper):
        left = self.symbol_table[left]
        right = self.symbol_table[right]
        # 32 -> 64
        if left.type == VarType.FLOAT32:
            self.increase_type(left.name, get_llvm_type_str(left.type),"double")
            left.type = VarType.FLOAT64
            left.name = '%' + str(self.reg - 1)
        elif left.type == VarType.INT32:
            self.increase_type(left.name, get_llvm_type_str(left.type), "i64")
            left.type = VarType.INT64
            left.name = '%' + str(self.reg - 1)
        if right.type == VarType.FLOAT32:
            self.increase_type(right.name, get_llvm_type_str(right.type),"double")
            right.type = VarType.FLOAT64
            right.name = '%' + str(self.reg - 1)
        elif right.type == VarType.INT32:
            self.increase_type(right.name, get_llvm_type_str(right.type), "i64")
            right.type = VarType.INT64
            right.name = '%' + str(self.reg - 1)
        
        # if left.type != right.type
        if left.type == VarType.FLOAT64 and right.type == VarType.INT64:
            self.int_to_float(right.name, get_llvm_type_str(right.type), 'double')
            right.name = '%' + str(self.reg - 1)
            right.type = VarType.FLOAT64
        elif left.type == VarType.INT64 and right.type == VarType.FLOAT64:
            self.int_to_float(left.name, get_llvm_type_str(left.type), 'double')
            left.name = '%' + str(self.reg - 1)
            left.type = VarType.FLOAT64
        
        if oper == '*':
            return self._multiply(left, right)
        else:
            return self._divide(left, right)

    def _multiply(self, left, right):
        if left.type == VarType.FLOAT64:
            self.code_text += "%" + str(self.reg) + " = fmul double " + str(left.name) + ", " + str(right.name) + "\n"
            self.reg += 1
            return VarType.FLOAT64
        else:
            self.code_text += "%" + str(self.reg) + " = mul i64 " + str(left.name) + ", " + str(right.name) + "\n"
            self.reg += 1
            return VarType.INT64

    def _divide(self, left, right):
        if left.type == VarType.FLOAT64:
            self.code_text += "%" + str(self.reg) + " = fdiv double " + str(left.name) + ", " + str(right.name) + "\n"
            self.reg += 1
            return VarType.FLOAT64
        else:
            self.code_text += "%" + str(self.reg) + " = sdiv i64 " + str(left.name) + ", " + str(right.name) + "\n"
            self.reg += 1
            return VarType.INT64

    def unary_operation(self, factor):
        self.xor_operation(factor, Value('true', 3), None, None)


    def write_operation(self, identifier, line, sym):
        value = self.get_value(identifier, line)
        if value.type == VarType.INT32 or value.type == VarType.INT64:
            self.code_text += f"%{self.reg} = load {self.get_llvm_type(value.type)}, {self.get_llvm_type(value.type)}* {sym}{identifier}\n" #tu add @ or %
            self.reg += 1
            self.code_text += f"%{self.reg} = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), {self.get_llvm_type(value.type)} %{self.reg - 1})\n"
            
          
        elif value.type == VarType.FLOAT32 or value.type == VarType.FLOAT64:
            self.code_text += f"%{self.reg} = load {self.get_llvm_type(value.type)}, {self.get_llvm_type(value.type)}* {sym}{identifier}\n"
            self.reg += 1
            self.code_text += f"%{self.reg} = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), {self.get_llvm_type(value.type)} %{self.reg - 1})\n"
          
        elif value.type == VarType.STRING:
            self.code_text += f"%{self.reg} = load {self.get_llvm_type(value.type)}*, {self.get_llvm_type(value.type)}** %{value.name}\n"
            self.reg += 1
            self.code_text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), {self.get_llvm_type(value.type)}* %{self.reg - 1})\n"
     
        elif value.type == VarType.BOOL:
            self.code_text += f"%{self.reg} = load i1, i1* {sym}{identifier}\n"
            self.reg += 1
            bool_str = f"{self.reg}"
            self.code_text += f"%{bool_str} = select i1 %{self.reg - 1}, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @trueStr, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @falseStr, i32 0, i32 0)\n"
            self.reg += 1
            self.code_text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %{bool_str})\n"

        self.reg += 1
        self.code_text += f"%{self.reg} = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0\n"
        self.code_text += f"call i32 (i8*, ...) @printf(i8* %{self.reg})\n"
        self.reg += 2
        

    def if_start(self):
        self.br += 1
        self.code_text += "br i1 %"+str(self.reg-1)+", label %true"+ str(self.br) +", label %false"+ str(self.br) +"\n"
        self.code_text += "true"+ str(self.br) +":\n"
        self.br_stack.append(self.br)

    def if_end(self):
        b = self.br_stack.pop()
        self.code_text += "br label %false"+ str(b) +"\n"
        self.code_text += "false" + str(b) + ":\n"
    
    
    def repeat_start(self, num):
        self.declare_int32('%' + str(self.reg), False)
        rep_count = self.reg
        self.reg += 1
        self.code_text += "store i32 " + str(0) + ", i32* " + str('%' + str(rep_count)) + "\n"
        
        self.br += 1
        self.code_text += f"br label %cond{str(self.br)}\n"
        self.code_text += f"cond{self.br}:\n"

        self.load(f"%{str(rep_count)}", 'i32')
        self.code_text += "%" + str(self.reg) + " = add i32 " + str("%"+str(self.reg-1)) + ", " + str(1) + "\n"
        self.reg += 1
        self.code_text += "store i32 " + str("%"+str(self.reg-1)) + ", i32* " + str('%'+str(rep_count)) + "\n"
        
        self.code_text += f"%{str(self.reg)} = icmp slt i32 %{str(self.reg-2)}, {str(num)}\n"
        self.reg += 1

        self.code_text += f"br i1 %{str(self.reg-1)}, label %true{str(self.br)}, label %false{str(self.br)}\n"
        self.code_text += f"true{str(self.br)}:\n"
        self.br_stack.append(self.br)
        


    def repeat_end(self):
        right = self.br_stack.pop()
        self.code_text += "br label %cond" + str(right) + "\n"
        self.code_text += "false" + str(right) + ":\n"


    def func_start(self, name, type):
        self.result_code += self.code_text
        self.mreg = self.reg
        self.code_text = "define " + str(type) + " @"+str(name)+"() nounwind {\n"
        self.reg = 1
    
    def func_end(self, type):
        self.code_text += "ret " + str(type) + " %" + str(self.reg-1) + "\n"
        self.code_text += "}\n"
        self.header_text += self.code_text
        self.code_text = ""
        self.reg = self.mreg

    def function_call(self, ident, type):
        self.code_text += "%" + str(self.reg) + " = call " + str(type) + " @" + str(ident) + "()\n"
        self.reg += 1


    def method_start(self, ident, type, className):
        self.result_code += self.code_text
        self.mreg = self.reg
        self.code_text = "define " + str(type) + " @"+str(ident)+f"(%{className}* %this) " + "nounwind {\n"
        self.reg = 1

    def call_method(self,  className, methodName, ident, type):
        self.code_text += f"%{self.reg} = getelementptr %{className}, %{className}* {ident}\n"
        self.reg += 1
        self.code_text += f"%{self.reg} = call {type} @{methodName} (ptr %{self.reg - 1})\n"
        self.reg += 1

    def read_int32(self, ident):
        self.code_text += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32* " + str(ident) + ")\n"
        self.reg += 1

    def read_int64(self, ident):
        self.code_text += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64* " + str(ident) + ")\n"
        self.reg += 1

    def read_float32(self, ident):
        self.code_text += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strf, i32 0, i32 0), float* " + str(ident) + ")\n"
        self.reg += 1

    def read_float64(self, ident):
        self.code_text += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strlf, i32 0, i32 0), double* " + str(ident) + ")\n"
        self.reg += 1

    def read_bool(self, ident):
        tempIntVar = "tempInt" + str(self.reg)
        self.code_text += "%" + tempIntVar + " = alloca i32\n"
        self.reg += 1
        self.code_text += "call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* " + tempIntVar + ")\n"
        self.reg += 1
        self.code_text += "%" + str(self.reg) + " = load i32, i32* " + tempIntVar + "\n"
        loadedIntVar = self.reg
        self.reg += 1
        self.code_text += "%" + str(self.reg) + " = icmp ne i32 " + str(loadedIntVar) + ", 0\n"
        self.code_text += "store i1 %" + str(self.reg) + ", i1* " + ident + "\n"
        self.reg += 1

    def read_string(self, ident):
        self.code_text += "%"+str(self.str)+" = alloca ["+str(17)+" x i8]\n"
        ident = str(ident)
        self.code_text += "%"+str(self.reg)+" = getelementptr inbounds ["+str(ident+1)+" x i8], ["+str(ident+1)+" x i8]* %str"+str(self.str)+", i64 0, i64 0\n"
        self.reg += 1
        self.code_text += "store i8* %"+str(self.reg-1)+", i8** "+id+"\n"
        self.str += 1
        self.code_text += "%"+str(self.reg)+" = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @strss, i32 0, i32 0), i8* "+str(self.reg-1)+")\n"
        self.reg += 1


    # assign i8 value
    def assign_string(self, ident, value, global_var):
        if ident not in self.symbol_table.keys():
            self.declare_string(ident, global_var)
            value = self.check_types(VarType.STRING, value)
        self.code_text += "store i8* %"+str(self.reg-1)+", i8** "+str(ident)+"\n"   

 
    # assign boolean value
    def assign_bool(self, ident, value, global_var):
        if ident not in self.symbol_table.keys():
            self.declare_bool(ident, global_var)
        self.code_text += "store i1 " + str(value) + ", i1* " + str(ident) + "\n"        # else:
    
    def assign_func(self, ident, value):
        self.code_text += "store i32 " + str(value) + ", i32* " + str(ident) + "\n"


    # assign i32 value
    def assign_i32(self, ident, value, global_var):
        if ident not in self.symbol_table.keys():
            self.declare_int32(ident, global_var)
            value = self.check_types(VarType.INT32, value)
        self.code_text += "store i32 " + str(value.name) + ", i32* " + str(ident) + "\n"
    
    # assign i64 value
    def assign_i64(self, ident, value, global_var):
        if ident not in self.symbol_table.keys():
            self.declare_int64(ident, global_var)
            value = self.check_types(VarType.INT64, value)
        self.code_text += "store i64 " + str(value.name) + ", i64* " + str(ident) + "\n"
    
    # assign float32 value
    def assign_float32(self, ident, value, global_var):
        if ident not in self.symbol_table.keys():
            self.declare_float32(ident, global_var)
            value = self.check_types(VarType.FLOAT32, value)
        import struct
        p = struct.pack('>d', float(value.name))
        hex_rep = p.hex()
        formatted = '0x' + hex_rep.upper()
        self.code_text += "store float " + str(formatted) + ", float* " + str(ident) + "\n"

    # assign double value
    def assign_double(self, ident, value, global_var):
        if ident not in self.symbol_table.keys():
            self.declare_float64(ident, global_var)
            value = self.check_types(VarType.FLOAT64, value)
        self.code_text += "store double " + str(value.name) + ", double* " + str(ident) + "\n"
    
    def assign_struct(self, ident, name, is_global):
        if is_global:
            self.header_text += f"{ident} = global %{name} zeroinitializer\n"
        else:
            self.code_text += f"{ident} = alloca %{name}\n"
    
    def assign_struct_field(self, ident, name, index, value, type):
        self.code_text += f"%{self.reg} = getelementptr %{name}, %{name}* {ident}, i32 0, i32 {index}\n"
        self.code_text += f"store {type} {value}, {type}* %{self.reg}\n"
        self.reg += 1
    
    def struct_field_access(self, ident, name, index, type):
        self.code_text += f"%{self.reg} = getelementptr %{name}, %{name}* {ident}, i32 0, i32 {index}\n"
        self.reg += 1
        self.code_text += f"%{self.reg} = load {type}, {type}* %{self.reg - 1}\n"
        self.reg += 1

    def check_types(self, type, value):
        if type != value.type and value.name[0] == '%':
            if type in [VarType.INT32, VarType.INT64] and value.type in [VarType.FLOAT32, VarType.FLOAT64]:
                self.float_to_int(str(value.name), get_llvm_type_str(value.type),
                                           get_llvm_type_str(type))
            elif type in [VarType.FLOAT32, VarType.FLOAT64] and value.type in [VarType.INT32, VarType.INT64]:
                self.int_to_float(str(value.name), get_llvm_type_str(value.type),
                                           get_llvm_type_str(type))
            elif type == VarType.FLOAT32 and value.type == VarType.FLOAT64:
                self.float32_to_64(str(value.name))
            elif type.value > value.type.value:
                self.increase_type(str(value.name), get_llvm_type_str(value.type),
                                             get_llvm_type_str(type))
            elif type.value < value.type.value:
                self.decrease_type(str(value.name), get_llvm_type_str(value.type),
                                             get_llvm_type_str(type))
                
            value.name = "%" + str(self.reg - 1)
            
        return value
        

    def declare_int32(self, ident, globalVar=False):
        # self.code_text += "%" + str(ident) + " = alloca i32\n"
        if globalVar:
            ident = ident.replace("%", "@") if "%" in ident else ident
            self.header_text += str(ident) + " = global i32 0\n"
        else:
            self.code_text += str(ident) + " = alloca i32\n"
                

    def declare_int64(self, ident, global_var):
        # self.code_text += "%" + str(ident) + " = alloca i64\n"
        if global_var:
            ident = ident.replace("%", "@") if "%" in ident else ident
            self.header_text += str(ident) + "  = global i64 0\n"
        else:
            self.code_text += str(ident) + " = alloca i64\n"


    def declare_float32(self, ident, global_var):
        # self.code_text += "%" + str(ident) + " = alloca float\n"
        if global_var:
            ident = ident.replace("%", "@") if "%" in ident else ident
            self.header_text += "@"+ str(ident) + " = global float 0.0\n"
        else:
            self.code_text += str(ident) + " = alloca float\n"


    def declare_float64(self, ident, global_var):
        # self.code_text += "%" + str(ident) + " = alloca double\n"
        if global_var:
            ident = ident.replace("%", "@") if "%" in ident else ident
            self.header_text += str(ident) + " = global double 0.0\n"
        else:
            self.code_text += str(ident) + " = alloca double\n"


    def declare_bool(self, ident, global_var):
        # self.code_text += "%" + str(ident) + " = alloca i1\n"
        if global_var:
            ident = ident.replace("%", "@") if "%" in ident else ident
            self.header_text += str(ident) + " = global i1 0\n"
        else:
            self.code_text += str(ident) + " = alloca i1\n"


    def declare_string(self, ident, global_var):
        # self.code_text += "%" + str(ident) + " = alloca i8*\n"
        if global_var:
            ident = ident.replace("%", "@") if "%" in ident else ident
            self.header_text += str(ident) + " = global [1 x i8] c\"\\00\"\n"
        else:
            self.code_text += str(ident) + "= alloca i8*\n"

    def allocate_string(self, ident, l):
        self.code_text += "%"+str(ident)+" = alloca ["+str(l+1)+" x i8]\n"
    
    def constant_string(self, content):
        l = len(content)+1
        l = str(l)
        self.header_text += "@str"+str(self.str)+" = constant ["+l+" x i8] c\""+content+"\\00\"\n"
        n = "str"+str(self.str)
        self.allocate_string(n, int(l)-1)
        self.code_text += "%"+str(self.reg)+" = bitcast ["+l+" x i8]* %"+n+" to i8*\n"
        self.code_text += "call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %"+str(self.reg)+", i8* align 1 getelementptr inbounds (["+l+" x i8], ["+l+" x i8]* @"+n+", i32 0, i32 0), i64 "+l+", i1 false)\n"
        self.reg += 1
        self.code_text += "%ptr"+n+" = alloca i8*\n"
        self.code_text += "%"+str(self.reg)+" = getelementptr inbounds ["+l+" x i8], ["+l+" x i8]* %"+n+", i64 0, i64 0\n"
        self.reg += 1
        self.code_text += "store i8* %"+str(self.reg-1)+", i8** %ptr"+n+"\n"
        self.str += 1

    def get_llvm_type(self, var_type):
        if var_type == VarType.INT32:
            return "i32"
        elif var_type == VarType.INT64:
            return "i64"
        elif var_type == VarType.FLOAT32:
            return "float"
        elif var_type == VarType.FLOAT64:
            return "double"
        elif var_type == VarType.BOOL:
            return "i1"
        elif var_type == VarType.STRING:
            return "i8"
        
    

    def get_value(self, identifier, line):
        if identifier in self.symbol_table:
            return self.symbol_table[identifier]
        else:
            print(f"Error on line {str(line)}: variable does not exist.")

    def increase_type(self, name, current, type):
        self.code_text += "%" + str(self.reg) + " = sext " + str(current) + " " + str(name) + " to " + str(type) + "\n"
        self.reg += 1
    
    def decrease_type(self, name, current, target_type):
        self.code_text += "%" + str(self.reg) + " = trunc " + str(current) + " " + str(name) + " to " + str(target_type) + "\n"
        self.reg += 1
    
    def int_to_float(self, name, current, type):
        self.code_text += "%" + str(self.reg) + " = uitofp " + str(current) + " " + str(name) + " to " + str(type) + "\n"
        self.reg += 1

    def float_to_int(self, name, current, type):
        self.code_text += "%" + str(self.reg) + " = fptosi " + str(current) + " " + str(name) + " to " + str(type) + "\n"
        self.reg += 1
    
    def float32_to_64(self, ident):
        self.code_text += "%" + str(self.reg) + " = fptrunc double " + str(ident) + " to float\n"
        self.reg += 1
    
    def load(self, ident, type):
        self.code_text += "%" + str(self.reg) + " = load " + str(type) + ", ptr " + str(ident) + "\n"
        self.reg += 1

    def finish(self):
        self.result_code += self.code_text

    def generate_code(self):
        text = "\n\n\n"
        text += "declare i32 @printf(ptr, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += "@strss = constant [5 x i8] c\"%10s\\00\"\n"
        text += "@strf = constant [3 x i8] c\"%f\\00\"\n"
        text += "@strpl = constant [5 x i8] c\"%lld\\00\"\n"
        text += "@strlf = constant [4 x i8] c\"%lf\\00\"\n"
        text += "@strhhd = constant [5 x i8] c\"%hhd\\00\"\n"
        text += "@strhd = constant [4 x i8] c\"%hd\\00\"\n"
        text += "@trueStr = constant [5 x i8] c\"true\\00\"\n"
        text += "@falseStr = constant [6 x i8] c\"false\\00\"\n"
        text += "@strps = constant [4 x i8] c\"%s\\0A\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.result_code
        text += "ret i32 0 }\n"
        return text
