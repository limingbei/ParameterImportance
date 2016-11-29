from collections import OrderedDict

from importance.evaluator.base_evaluator import AbstractEvaluator


class fANOVA(AbstractEvaluator):

    def __init__(self, scenario, cs, model, to_evaluate: int, **kwargs):
        super().__init__(scenario, cs, model, to_evaluate, **kwargs)
        self.name = 'fANOVA'

    def plot_result(self):
        pass

    def run(self) -> OrderedDict:
        raise NotImplementedError
        # fanova.get_marginal list dimension list / position of parameters in configspace to analyze

        # for parameter in self.to_evaluate:
        #     get_idx in ordered_dict_of_config_space
        #     imp_val_of_param[parameter] = fanova.get_marginal(dim_list=[idx])
