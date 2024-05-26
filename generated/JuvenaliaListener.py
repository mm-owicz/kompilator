# Generated from Juvenalia.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .JuvenaliaParser import JuvenaliaParser
else:
    from JuvenaliaParser import JuvenaliaParser

# This class defines a complete listener for a parse tree produced by JuvenaliaParser.
class JuvenaliaListener(ParseTreeListener):

    # Enter a parse tree produced by JuvenaliaParser#prog.
    def enterProg(self, ctx:JuvenaliaParser.ProgContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#prog.
    def exitProg(self, ctx:JuvenaliaParser.ProgContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#write.
    def enterWrite(self, ctx:JuvenaliaParser.WriteContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#write.
    def exitWrite(self, ctx:JuvenaliaParser.WriteContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#read.
    def enterRead(self, ctx:JuvenaliaParser.ReadContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#read.
    def exitRead(self, ctx:JuvenaliaParser.ReadContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#exprression.
    def enterExprression(self, ctx:JuvenaliaParser.ExprressionContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#exprression.
    def exitExprression(self, ctx:JuvenaliaParser.ExprressionContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#assign.
    def enterAssign(self, ctx:JuvenaliaParser.AssignContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#assign.
    def exitAssign(self, ctx:JuvenaliaParser.AssignContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#elementAssign.
    def enterElementAssign(self, ctx:JuvenaliaParser.ElementAssignContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#elementAssign.
    def exitElementAssign(self, ctx:JuvenaliaParser.ElementAssignContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#arrAssign.
    def enterArrAssign(self, ctx:JuvenaliaParser.ArrAssignContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#arrAssign.
    def exitArrAssign(self, ctx:JuvenaliaParser.ArrAssignContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#repeatStatement.
    def enterRepeatStatement(self, ctx:JuvenaliaParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#repeatStatement.
    def exitRepeatStatement(self, ctx:JuvenaliaParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#ifStatement.
    def enterIfStatement(self, ctx:JuvenaliaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#ifStatement.
    def exitIfStatement(self, ctx:JuvenaliaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#funcDecl.
    def enterFuncDecl(self, ctx:JuvenaliaParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#funcDecl.
    def exitFuncDecl(self, ctx:JuvenaliaParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structDeclaration.
    def enterStructDeclaration(self, ctx:JuvenaliaParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structDeclaration.
    def exitStructDeclaration(self, ctx:JuvenaliaParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structFieldAssignment.
    def enterStructFieldAssignment(self, ctx:JuvenaliaParser.StructFieldAssignmentContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structFieldAssignment.
    def exitStructFieldAssignment(self, ctx:JuvenaliaParser.StructFieldAssignmentContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structAssignmet.
    def enterStructAssignmet(self, ctx:JuvenaliaParser.StructAssignmetContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structAssignmet.
    def exitStructAssignmet(self, ctx:JuvenaliaParser.StructAssignmetContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JuvenaliaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JuvenaliaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#classAssignment.
    def enterClassAssignment(self, ctx:JuvenaliaParser.ClassAssignmentContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#classAssignment.
    def exitClassAssignment(self, ctx:JuvenaliaParser.ClassAssignmentContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#arrayAssign.
    def enterArrayAssign(self, ctx:JuvenaliaParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#arrayAssign.
    def exitArrayAssign(self, ctx:JuvenaliaParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#expr.
    def enterExpr(self, ctx:JuvenaliaParser.ExprContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#expr.
    def exitExpr(self, ctx:JuvenaliaParser.ExprContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#condXorStm.
    def enterCondXorStm(self, ctx:JuvenaliaParser.CondXorStmContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#condXorStm.
    def exitCondXorStm(self, ctx:JuvenaliaParser.CondXorStmContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#condStmAnd.
    def enterCondStmAnd(self, ctx:JuvenaliaParser.CondStmAndContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#condStmAnd.
    def exitCondStmAnd(self, ctx:JuvenaliaParser.CondStmAndContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#condStmRel.
    def enterCondStmRel(self, ctx:JuvenaliaParser.CondStmRelContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#condStmRel.
    def exitCondStmRel(self, ctx:JuvenaliaParser.CondStmRelContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#addExpr.
    def enterAddExpr(self, ctx:JuvenaliaParser.AddExprContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#addExpr.
    def exitAddExpr(self, ctx:JuvenaliaParser.AddExprContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#multExpr.
    def enterMultExpr(self, ctx:JuvenaliaParser.MultExprContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#multExpr.
    def exitMultExpr(self, ctx:JuvenaliaParser.MultExprContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#negFactor.
    def enterNegFactor(self, ctx:JuvenaliaParser.NegFactorContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#negFactor.
    def exitNegFactor(self, ctx:JuvenaliaParser.NegFactorContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#factor.
    def enterFactor(self, ctx:JuvenaliaParser.FactorContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#factor.
    def exitFactor(self, ctx:JuvenaliaParser.FactorContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#ifStm.
    def enterIfStm(self, ctx:JuvenaliaParser.IfStmContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#ifStm.
    def exitIfStm(self, ctx:JuvenaliaParser.IfStmContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#blockIf.
    def enterBlockIf(self, ctx:JuvenaliaParser.BlockIfContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#blockIf.
    def exitBlockIf(self, ctx:JuvenaliaParser.BlockIfContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#repeatStm.
    def enterRepeatStm(self, ctx:JuvenaliaParser.RepeatStmContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#repeatStm.
    def exitRepeatStm(self, ctx:JuvenaliaParser.RepeatStmContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#repNum.
    def enterRepNum(self, ctx:JuvenaliaParser.RepNumContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#repNum.
    def exitRepNum(self, ctx:JuvenaliaParser.RepNumContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#blockRepeat.
    def enterBlockRepeat(self, ctx:JuvenaliaParser.BlockRepeatContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#blockRepeat.
    def exitBlockRepeat(self, ctx:JuvenaliaParser.BlockRepeatContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#function.
    def enterFunction(self, ctx:JuvenaliaParser.FunctionContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#function.
    def exitFunction(self, ctx:JuvenaliaParser.FunctionContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#blockFun.
    def enterBlockFun(self, ctx:JuvenaliaParser.BlockFunContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#blockFun.
    def exitBlockFun(self, ctx:JuvenaliaParser.BlockFunContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#classDecl.
    def enterClassDecl(self, ctx:JuvenaliaParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#classDecl.
    def exitClassDecl(self, ctx:JuvenaliaParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#blockClass.
    def enterBlockClass(self, ctx:JuvenaliaParser.BlockClassContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#blockClass.
    def exitBlockClass(self, ctx:JuvenaliaParser.BlockClassContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#method.
    def enterMethod(self, ctx:JuvenaliaParser.MethodContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#method.
    def exitMethod(self, ctx:JuvenaliaParser.MethodContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#blockMethod.
    def enterBlockMethod(self, ctx:JuvenaliaParser.BlockMethodContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#blockMethod.
    def exitBlockMethod(self, ctx:JuvenaliaParser.BlockMethodContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#methodType.
    def enterMethodType(self, ctx:JuvenaliaParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#methodType.
    def exitMethodType(self, ctx:JuvenaliaParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#methodName.
    def enterMethodName(self, ctx:JuvenaliaParser.MethodNameContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#methodName.
    def exitMethodName(self, ctx:JuvenaliaParser.MethodNameContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#className.
    def enterClassName(self, ctx:JuvenaliaParser.ClassNameContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#className.
    def exitClassName(self, ctx:JuvenaliaParser.ClassNameContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#methodCall.
    def enterMethodCall(self, ctx:JuvenaliaParser.MethodCallContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#methodCall.
    def exitMethodCall(self, ctx:JuvenaliaParser.MethodCallContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#classAssign.
    def enterClassAssign(self, ctx:JuvenaliaParser.ClassAssignContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#classAssign.
    def exitClassAssign(self, ctx:JuvenaliaParser.ClassAssignContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structDecl.
    def enterStructDecl(self, ctx:JuvenaliaParser.StructDeclContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structDecl.
    def exitStructDecl(self, ctx:JuvenaliaParser.StructDeclContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#blockStruct.
    def enterBlockStruct(self, ctx:JuvenaliaParser.BlockStructContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#blockStruct.
    def exitBlockStruct(self, ctx:JuvenaliaParser.BlockStructContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structVarDecl.
    def enterStructVarDecl(self, ctx:JuvenaliaParser.StructVarDeclContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structVarDecl.
    def exitStructVarDecl(self, ctx:JuvenaliaParser.StructVarDeclContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structAssign.
    def enterStructAssign(self, ctx:JuvenaliaParser.StructAssignContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structAssign.
    def exitStructAssign(self, ctx:JuvenaliaParser.StructAssignContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structFieldAssign.
    def enterStructFieldAssign(self, ctx:JuvenaliaParser.StructFieldAssignContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structFieldAssign.
    def exitStructFieldAssign(self, ctx:JuvenaliaParser.StructFieldAssignContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structFieldAccess.
    def enterStructFieldAccess(self, ctx:JuvenaliaParser.StructFieldAccessContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structFieldAccess.
    def exitStructFieldAccess(self, ctx:JuvenaliaParser.StructFieldAccessContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#arrayAccess.
    def enterArrayAccess(self, ctx:JuvenaliaParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#arrayAccess.
    def exitArrayAccess(self, ctx:JuvenaliaParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#funcCall.
    def enterFuncCall(self, ctx:JuvenaliaParser.FuncCallContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#funcCall.
    def exitFuncCall(self, ctx:JuvenaliaParser.FuncCallContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#ident.
    def enterIdent(self, ctx:JuvenaliaParser.IdentContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#ident.
    def exitIdent(self, ctx:JuvenaliaParser.IdentContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#type.
    def enterType(self, ctx:JuvenaliaParser.TypeContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#type.
    def exitType(self, ctx:JuvenaliaParser.TypeContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#funType.
    def enterFunType(self, ctx:JuvenaliaParser.FunTypeContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#funType.
    def exitFunType(self, ctx:JuvenaliaParser.FunTypeContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#funName.
    def enterFunName(self, ctx:JuvenaliaParser.FunNameContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#funName.
    def exitFunName(self, ctx:JuvenaliaParser.FunNameContext):
        pass


    # Enter a parse tree produced by JuvenaliaParser#structName.
    def enterStructName(self, ctx:JuvenaliaParser.StructNameContext):
        pass

    # Exit a parse tree produced by JuvenaliaParser#structName.
    def exitStructName(self, ctx:JuvenaliaParser.StructNameContext):
        pass



del JuvenaliaParser