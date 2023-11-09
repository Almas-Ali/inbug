'''
InBug - A debuger for your Python codes

Written by Md. Almas Ali
'''

from inspect import currentframe, getframeinfo
from typing import Final
import builtins


DEFAULT_PREFIX: Final = 'InBug: '


class InBugDebuger:
    '''InBug Debuger class'''

    def __init__(self, *args, **kwargs) -> None:
        self.prefix = DEFAULT_PREFIX

        self.args = args
        self.kwargs = kwargs

        # get all variables name from self.args
        if self.args:
            self.args_name_values = {}
            for arg in self.args:
                self.args_name_values[self._get_variable_name(arg)] = arg
        else:
            self.args_name_values = None

        # get all variables name from self.kwargs
        if self.kwargs:
            self.kwargs_name_values = {}
            for k, v in self.kwargs.items():
                self.kwargs_name_values[k] = v
        else:
            self.kwargs_name_values = None

        # get all variables name from the parent function
        try:
            self.parent_function_name = self._get_parent_function_name()
            self.parent_function = globals()[self.parent_function_name]
            self.parent_function_args_name_values = {}
            for arg in self.parent_function.__code__.co_varnames:
                self.parent_function_args_name_values[arg] = globals()[arg]
        except:
            self.parent_function_name = None
            self.parent_function_args_name_values = None

        if len(self.args) == 0 and len(self.kwargs) == 0:
            if self.parent_function_name is not None:
                print(
                    f'{self.prefix}| {self.parent_function_name}({self.parent_function_args_name_values})')
                return

        if len(self.args) > 0:
            if self.parent_function_name is not None:
                print(
                    f'{self.prefix}| {self.parent_function_name}({self.parent_function_args_name_values})')
            print(f'{self.prefix}| {self.args_name_values}')
            return

    def __str__(self) -> str:
        return 'InBug Debuger'

    def __repr__(self) -> str:
        return 'InBug Debuger'

    def _get_parent_function_name(self) -> str:
        '''
        Get the name of the parent function.
        '''
        caller = getframeinfo(currentframe().f_back)
        return caller.function

    def _get_variable_name(self, variable) -> str:
        '''
        Get the name of the variable
        '''
        frame = currentframe()
        try:
            for name, value in frame.f_back.f_back.f_locals.items():
                if value is variable:
                    return name
        finally:
            del frame

    def bug(self, message) -> None:
        '''
        Print the message with the file name and line number
        '''
        caller = getframeinfo(currentframe().f_back)
        # print(caller.filename, caller.lineno, message)
        print(f'{self.prefix}| {caller.filename}:{caller.lineno} | {message}')

    def ConfigureOutput(self, prefix: str = DEFAULT_PREFIX):
        '''
        Configure the output prefix
        '''
        self.prefix = prefix
        return self

    def enable(self) -> None:
        '''
        Enable the debuger
        '''
        builtins.print = self.bug

    def disable(self): ...
    def set_prefix(self, prefix): ...
    def set_output(self, output): ...
    def set_color(self, color): ...
    def set_background_color(self, background_color): ...


ib = InBugDebuger
