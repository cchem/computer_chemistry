from pathlib import Path


class MDOutputManager:
    def __init__(self, out_file, max_iter, logging_interval, config_file):
        self.out_file = Path(out_file)
        self.max_iter = max_iter
        self.interval = logging_interval
        self.config_file = Path(config_file)

    def exists(self):
        return self.out_file.exists()

    def is_finished(self):
        raise NotImplementedError

    def set_from_calculation_config(self):
        raise NotImplementedError

    def dump_config(self):
        if self.config_file.suffix == ".json":
            raise NotImplementedError
        else:
            raise RuntimeError(f"suffix {self.config_file.suffix} is not supported.")

    def restart(self):
        raise NotImplementedError


class MDSimulation:
    def __init__(self):
        return

    def initialize(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


class NVTEnsemble(MDSimulation):
    def __init__(self):
        super().__init__()
        return

    def initialize(self):
        return
