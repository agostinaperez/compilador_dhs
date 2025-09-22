// Generated from /home/agos/dhs/src/main/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link compiladoresParser}.
 */
public interface compiladoresListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void enterInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void exitInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#valor}.
	 * @param ctx the parse tree
	 */
	void enterValor(compiladoresParser.ValorContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#valor}.
	 * @param ctx the parse tree
	 */
	void exitValor(compiladoresParser.ValorContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(compiladoresParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(compiladoresParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#ipyc}.
	 * @param ctx the parse tree
	 */
	void enterIpyc(compiladoresParser.IpycContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#ipyc}.
	 * @param ctx the parse tree
	 */
	void exitIpyc(compiladoresParser.IpycContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#listavar}.
	 * @param ctx the parse tree
	 */
	void enterListavar(compiladoresParser.ListavarContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#listavar}.
	 * @param ctx the parse tree
	 */
	void exitListavar(compiladoresParser.ListavarContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#incremento}.
	 * @param ctx the parse tree
	 */
	void enterIncremento(compiladoresParser.IncrementoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#incremento}.
	 * @param ctx the parse tree
	 */
	void exitIncremento(compiladoresParser.IncrementoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void enterComparacion(compiladoresParser.ComparacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void exitComparacion(compiladoresParser.ComparacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#negacion}.
	 * @param ctx the parse tree
	 */
	void enterNegacion(compiladoresParser.NegacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#negacion}.
	 * @param ctx the parse tree
	 */
	void exitNegacion(compiladoresParser.NegacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#funcion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(compiladoresParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#funcion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(compiladoresParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(compiladoresParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(compiladoresParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#retorno}.
	 * @param ctx the parse tree
	 */
	void enterRetorno(compiladoresParser.RetornoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#retorno}.
	 * @param ctx the parse tree
	 */
	void exitRetorno(compiladoresParser.RetornoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#iif}.
	 * @param ctx the parse tree
	 */
	void enterIif(compiladoresParser.IifContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#iif}.
	 * @param ctx the parse tree
	 */
	void exitIif(compiladoresParser.IifContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#ielse}.
	 * @param ctx the parse tree
	 */
	void enterIelse(compiladoresParser.IelseContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#ielse}.
	 * @param ctx the parse tree
	 */
	void exitIelse(compiladoresParser.IelseContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(compiladoresParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(compiladoresParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void enterCiclo(compiladoresParser.CicloContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void exitCiclo(compiladoresParser.CicloContext ctx);
}