from autogoal.contrib.keras._generated import *
from autogoal.grammar import GraphGrammar, Path, Block, CfgInitializer, Epsilon


def build_grammar(preprocessing=False, reduction=False, features=False, features_time_distributed=False):
    modules = []

    if preprocessing:
        modules.append("PreprocessingModule")

    if reduction:
        modules.append("ReductionModule")

    if features:
        modules.append("FeaturesModule")

    if features_time_distributed:
        modules.append("FeaturesTimeDistributedModule")

    if (reduction or features) and features_time_distributed:
        raise ValueError("Cannot combine time-distributed modules with flat modules.")

    if not modules:
        raise ValueError("At least one module must be activated.")

    grammar = GraphGrammar(start=Path(*modules), initializer=CfgInitializer())

    grammar.add("PreprocessingModule", Path("Recurrent", "PreprocessingModule"))
    grammar.add("PreprocessingModule", Epsilon())
    grammar.add("Recurrent", Seq2SeqLSTM)
    grammar.add("Recurrent", Seq2SeqBiLSTM)

    grammar.add("ReductionModule", Seq2VecLSTM)
    grammar.add("ReductionModule", Seq2VecBiLSTM)

    grammar.add("FeaturesModule", Path("DenseLayer", "FeaturesModule"))
    grammar.add("FeaturesModule", Epsilon())
    grammar.add("DenseLayer", Block(Dense, "DenseLayer"))
    grammar.add("DenseLayer", Path(Dense, "DenseLayer"))
    grammar.add("DenseLayer", Epsilon())

    grammar.add("FeaturesTimeDistributedModule", Path("TDLayer", "FeaturesTimeDistributedModule"))
    grammar.add("FeaturesTimeDistributedModule", Epsilon())
    grammar.add("TDLayer", Block(TimeDistributed, "TDLayer"))
    grammar.add("TDLayer", Path(TimeDistributed, "TDLayer"))
    grammar.add("TDLayer", Epsilon())

    return grammar
