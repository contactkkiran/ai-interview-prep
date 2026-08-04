import ast


def extract_python_symbols(source_code):
    tree = ast.parse(source_code)
    symbols = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            symbols.append({
                "name": node.name,
                "symbol_type": "class",
                "start_line": node.lineno,
                "end_line": getattr(node, "end_lineno", node.lineno),
            })

        if isinstance(node, ast.FunctionDef):
            symbols.append({
                "name": node.name,
                "symbol_type": "function",
                "start_line": node.lineno,
                "end_line": getattr(node, "end_lineno", node.lineno),
            })

    return symbols

