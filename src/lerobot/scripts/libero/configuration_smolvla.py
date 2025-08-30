from transformers import PretrainedConfig
class SmolVLAConfig(PrismaticConfig):
    model_type: str = "smolvla"

    def __init__(
        self,
        norm_stats: Optional[Dict[str, Dict[str, Dict[str, Dict[str, List[float]]]]]] = None,
        n_action_bins: int = 256,
        **kwargs: str,
    ) -> None:
        self.norm_stats = norm_stats
        self.n_action_bins = n_action_bins

        super().__init__(**kwargs)

