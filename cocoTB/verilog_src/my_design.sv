`timescale 1 ns/1 ns
module my_design
#(parameter W = 32)
(
    input clk,
    input reset,
    input load,
    input [(W-1):0] data,
    output reg [(W-1):0] q
);

always @(posedge clk) begin
    if (reset)
        q <= 0;
    else if (load)
        q <= data;
    else
        q <= q +1;
end

endmodule