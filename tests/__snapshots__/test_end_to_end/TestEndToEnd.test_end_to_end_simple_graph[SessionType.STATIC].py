from lineapy import SessionType, Tracer, ExecutionMode

lineapy_tracer = Tracer(SessionType.STATIC, "[source file path]", ExecutionMode.MEMORY)
lineapy_tracer.trace_import(
    name="lineapy",
    syntax_dictionary={
        "lineno": 1,
        "col_offset": 0,
        "end_lineno": 1,
        "end_col_offset": 14,
    },
    alias=None,
)
lineapy_tracer.assign(
    variable_name="a",
    value_node=lineapy_tracer.call(
        function_name="abs",
        syntax_dictionary={
            "lineno": 2,
            "col_offset": 4,
            "end_lineno": 2,
            "end_col_offset": 11,
        },
        arguments=[
            lineapy_tracer.literal(
                11,
                {"lineno": 2, "col_offset": 8, "end_lineno": 2, "end_col_offset": 10},
            )
        ],
        keyword_arguments=[],
    ),
    syntax_dictionary={
        "lineno": 2,
        "col_offset": 0,
        "end_lineno": 2,
        "end_col_offset": 11,
    },
)
lineapy_tracer.publish(variable_name="a", description="testing artifact publish")
lineapy_tracer.exit()