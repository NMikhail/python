module my_design(
    input clk,
    input reset,
    input [7:0] data,
    output reg [7:0] q
);

always @(posedge clk) begin
    if (reset)
        q <= 0;
    else
        q <= data;
end

endmodule