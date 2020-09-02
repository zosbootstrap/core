from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        """ handler for file transfer operations """
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

        locsrc = self._task.args.get("src", None)
        rmtdest = self._task.args.get("dest", None)
        copy_args = {}

        copy_args.update(
          dict(
            dest='/tmp/pkg',
            src=locsrc,
           )
        )
        copy_res = self._execute_module(module_name='copy', module_args=copy_args, task_vars=task_vars)
