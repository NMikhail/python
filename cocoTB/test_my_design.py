import cocotb

from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, ReadOnly
from cocotb.result import TestFailure, ReturnValue

@cocotb.coroutine
def data(dut, value):
    yield RisingEdge(dut.clk)
    dut.data = value
    raise ReturnValue((dut.q.value))

@cocotb.coroutine
def reset_out(dut):
    dut.reset = 1
    yield Timer(35)
    dut.reset = 0

@cocotb.coroutine
def mmm(dut):

    yield RisingEdge(dut.clk)

@cocotb.test()
def test_ff(dut):
    width = dut.W.value.integer
    dut.log.info("Found FF by %d bits wide" % (width))
    #set clocks
    cocotb.fork(Clock(dut.clk, 10).start())
    cocotb.fork(reset_out(dut))
    cocotb.fork(mmm(dut))
    for i in xrange(2**5):
        yield data(dut, i)
        dut.log.info("Write data: %s Read data:  %s Reset: %s" % (dut.data.value, dut.q.value, dut.reset.value))

    if False:
        dut.log.error("Error")
        raise TestFailure
    dut.log.info("Read data OK")
