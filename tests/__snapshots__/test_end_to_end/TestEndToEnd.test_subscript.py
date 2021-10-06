import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="\nls = [1,2,3,4]\nls[0] = 1\na = 4\nls[1] = a\nls[2:3] = [30]\nls[3:a] = [40]\n",
    working_directory="dummy_linea_repo/",
    libraries=[],
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=2,
        col_offset=0,
        end_lineno=2,
        end_col_offset=14,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=2,
                    col_offset=6,
                    end_lineno=2,
                    end_col_offset=7,
                    value=1,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=2,
                    col_offset=8,
                    end_lineno=2,
                    end_col_offset=9,
                    value=2,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=2,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=2,
                    col_offset=10,
                    end_lineno=2,
                    end_col_offset=11,
                    value=3,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=3,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=2,
                    col_offset=12,
                    end_lineno=2,
                    end_col_offset=13,
                    value=4,
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="__build_list__",
        ).id,
    ).id,
    assigned_variable_name="ls",
)
call_2 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=9,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=variable_1.id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=3,
                col_offset=3,
                end_lineno=3,
                end_col_offset=4,
                value=0,
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=2,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=3,
                col_offset=8,
                end_lineno=3,
                end_col_offset=9,
                value=1,
            ).id,
        ).id,
    ],
    function_id=LookupNode(
        id=get_new_id(),
        session_id=session.id,
        name="setitem",
    ).id,
)
variable_2 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_node_id=LiteralNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=4,
        col_offset=0,
        end_lineno=4,
        end_col_offset=5,
        value=4,
    ).id,
    assigned_variable_name="a",
)
call_3 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=5,
    col_offset=0,
    end_lineno=5,
    end_col_offset=9,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=variable_1.id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=5,
                col_offset=3,
                end_lineno=5,
                end_col_offset=4,
                value=1,
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=2,
            value_node_id=variable_2.id,
        ).id,
    ],
    function_id=LookupNode(
        id=get_new_id(),
        session_id=session.id,
        name="setitem",
    ).id,
)
call_6 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=6,
    col_offset=0,
    end_lineno=6,
    end_col_offset=14,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=variable_1.id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=6,
                col_offset=3,
                end_lineno=6,
                end_col_offset=6,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=6,
                            col_offset=3,
                            end_lineno=6,
                            end_col_offset=4,
                            value=2,
                        ).id,
                    ).id,
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=1,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=6,
                            col_offset=5,
                            end_lineno=6,
                            end_col_offset=6,
                            value=3,
                        ).id,
                    ).id,
                ],
                function_id=LookupNode(
                    id=get_new_id(),
                    session_id=session.id,
                    name="slice",
                ).id,
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=2,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=6,
                col_offset=10,
                end_lineno=6,
                end_col_offset=14,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=6,
                            col_offset=11,
                            end_lineno=6,
                            end_col_offset=13,
                            value=30,
                        ).id,
                    ).id
                ],
                function_id=LookupNode(
                    id=get_new_id(),
                    session_id=session.id,
                    name="__build_list__",
                ).id,
            ).id,
        ).id,
    ],
    function_id=LookupNode(
        id=get_new_id(),
        session_id=session.id,
        name="setitem",
    ).id,
)
call_9 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=7,
    col_offset=0,
    end_lineno=7,
    end_col_offset=14,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=variable_1.id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=7,
                col_offset=3,
                end_lineno=7,
                end_col_offset=6,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=7,
                            col_offset=3,
                            end_lineno=7,
                            end_col_offset=4,
                            value=3,
                        ).id,
                    ).id,
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=1,
                        value_node_id=variable_2.id,
                    ).id,
                ],
                function_id=LookupNode(
                    id=get_new_id(),
                    session_id=session.id,
                    name="slice",
                ).id,
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=2,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=7,
                col_offset=10,
                end_lineno=7,
                end_col_offset=14,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=7,
                            col_offset=11,
                            end_lineno=7,
                            end_col_offset=13,
                            value=40,
                        ).id,
                    ).id
                ],
                function_id=LookupNode(
                    id=get_new_id(),
                    session_id=session.id,
                    name="__build_list__",
                ).id,
            ).id,
        ).id,
    ],
    function_id=LookupNode(
        id=get_new_id(),
        session_id=session.id,
        name="setitem",
    ).id,
)
