from llvmlite import ir
import llvmlite.binding as llvm
import ctypes

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()


def print_wrapper(x):
    print("Got value", x)


printfn_type = ctypes.CFUNCTYPE(None, ctypes.c_int64)
printfn = printfn_type(print_wrapper)

llvm.add_symbol(
    "print",
    ctypes.cast(printfn, ctypes.c_void_p).value)


def create_execution_engine():
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_module = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_module, target_machine)
    return engine


def create_module():
    i64_type = ir.IntType(bits=64)
    i64_ptr_type = ir.PointerType(i64_type)
    bool_type = ir.IntType(bits=1)

    module = ir.Module(name="test")
    print_func = ir.Function(
        module,
        ir.FunctionType(args=(i64_type,), return_type=ir.VoidType()),
        name="print")

    # TODO: write and add functions "is_prime" and "calc_primes" to the module.
    # Please do not modify the rest of the source code.

    return module


module = create_module()
# print("---- Compiled module ----")
# print(module)
# print("---- Compiled module ----")

with create_execution_engine() as ee:
    mod = llvm.parse_assembly(str(module))
    mod.verify()

    pass_manager = llvm.PassManagerBuilder()
    pass_manager.opt_level = 3
    module_pass = llvm.ModulePassManager()
    pass_manager.populate(module_pass)
    module_pass.run(mod)

    ee.add_module(mod)
    ee.finalize_object()
    ee.run_static_constructors()

    is_prime_ptr = ee.get_function_address("is_prime")
    is_prime = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_int64)(is_prime_ptr)
    sum_primes_ptr = ee.get_function_address("sum_primes")
    sum_primes = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64)(sum_primes_ptr)

    primes = [i for i in range(100) if is_prime(i)]
    print("Primes:", primes)
    print("Sum of primes:", sum(primes))

    a = list(range(100))
    sum_primes((ctypes.c_int64 * len(a))(*a), len(a))
