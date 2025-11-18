from pyuvm import *

from uvc.sdt.src.cl_sdt_config import *
from uvc.apb.src.cl_apb_config import *

from uvc.sdt.src import cl_sdt_interface
from uvc.sdt.src.sdt_common import DriverType

class cl_marb_tb_config(uvm_object):
    # Added dut to constructor so that we could instantiate vif here in config (as Jacob showed)
    def __init__(self, name = "cl_marb_tb_config", dut=None):
        super().__init__(name)
        self.dut = dut

        self.apb_cfg             = cl_apb_config.create("apb_cfg")

        # Create and configure three producer configuration objects - clients
        self.sdt_prod1_cfg              = cl_sdt_config.create("sdt_prod1_cfg")
        self.sdt_prod1_cfg.vif          = cl_sdt_interface(self.dut.clk,
                                                           self.dut.rst,
                                                           "producer1_vif")     # Instantiate interface
        self.sdt_prod1_cfg.is_active    = uvm_active_passive_enum.UVM_ACTIVE   # Active because producer
        self.sdt_prod1_cfg.driver       = DriverType.PRODUCER
        self.sdt_prod1_cfg.seq_item_override = SequenceItemOverride.USER_DEFINED # Enable factory override

        # TODO what about self.num_consumer_seq 

        self.sdt_prod2_cfg = cl_sdt_config.create("sdt_prod2_cfg")
        self.sdt_prod2_cfg.vif = cl_sdt_interface(self.dut.clk,
                                                  self.dut.rst,
                                                  name="producer2_vif")
        self.sdt_prod2_cfg.is_active    = uvm_active_passive_enum.UVM_ACTIVE   # Active because producer
        self.sdt_prod2_cfg.driver       = DriverType.PRODUCER
        self.sdt_prod2_cfg.seq_item_override = SequenceItemOverride.USER_DEFINED

        self.sdt_prod3_cfg = cl_sdt_config.create("sdt_prod3_cfg")
        self.sdt_prod3_cfg.vif = cl_sdt_interface(self.dut.clk,
                                                  self.dut.rst,
                                                  name="producer3_vif")
        self.sdt_prod3_cfg.is_active    = uvm_active_passive_enum.UVM_ACTIVE   # Active because producer
        self.sdt_prod3_cfg.driver       = DriverType.PRODUCER
        self.sdt_prod3_cfg.seq_item_override = SequenceItemOverride.USER_DEFINED

        # Create one consumer cfgs - memory
        self.sdt_cons_cfg = cl_sdt_config.create("sdt_cons_cfg")
        self.sdt_cons_cfg.vif = cl_sdt_interface(self.dut.clk,
                                                 self.dut.rst,
                                                 name="consumer_vif")
        self.sdt_cons_cfg.is_active    = uvm_active_passive_enum.UVM_ACTIVE   # Still needs to be active to receive data
        self.sdt_cons_cfg.driver       = DriverType.CONSUMER
        self.sdt_cons_cfg.seq_item_override = SequenceItemOverride.USER_DEFINED

        
        
        