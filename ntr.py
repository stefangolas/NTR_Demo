import time
from tip_tracker import TipTracker
import sys
import os

def sleep(secs):
        time.sleep(secs)
        return None

from pyhamilton import (LayoutManager, HamiltonInterface, aspirate, dispense, tip_pick_up, tip_eject,
        tip_pick_up_96, tip_eject_96, aspirate_96, dispense_96, normal_logging, oemerr,
        Plate96, Tip96, initialize, resource_list_with_prefix, ResourceType,
        hhs_create_star_device, hhs_set_plate_lock, hhs_start_shaker, hhs_stop_shaker,
        hhs_start_temp_ctrl, hhs_stop_temp_ctrl)


lmgr = LayoutManager('FN Deck Layout.lay')

tip_tracker_NTR50_ch = TipTracker('NTR50_channels.json',
                        'FN Deck Layout.lay',
                        'Waste_NTR50',
                        'COREGripTool_OnWaste_1000ul_0001',
                        gripHeight = 5,
                        gripWidth = 90,
                        openWidth = 100)

tip_tracker_NTR50_ch.run_editor()

tip_tracker_NTR300_ch = TipTracker('NTR300_channels.json',
                        'FN Deck Layout.lay',
                        'Waste_NTR50',
                        'COREGripTool_OnWaste_1000ul_0001',
                        gripHeight = 5,
                        gripWidth = 90,
                        openWidth = 100)

tip_tracker_NTR300_ch.run_editor()

tip_tracker_NTR50_MPH = TipTracker('NTR50_MPH.json',
                       'FN Deck Layout.lay',
                       'Waste_NTR50',
                       'COREGripTool_OnWaste_1000ul_0001',
                       gripHeight = 5,
                       gripWidth = 90,
                       openWidth = 100)
tip_tracker_NTR50_MPH.run_editor()




if __name__ == '__main__':
    with HamiltonInterface(simulate=True) as ham_int:
        initialize(ham_int)
        normal_logging(ham_int, os.getcwd())

        tip_tracker_NTR50_MPH.apply_interface(ham_int)
        tip_tracker_NTR50_ch.apply_interface(ham_int)
        tip_tracker_NTR300_ch.apply_interface(ham_int)


        for i in range(8):
            # NTR50 MPH
            tip_tracker_NTR50_MPH.get_96_tips()
            tip_eject_96(ham_int)
            
            
        for i in range(90):
            # NTR50 Channels
            tip_tracker_NTR50_ch.get_tips(8)
            tip_eject(ham_int)
            
            # NTR300 MPH
            tip_tracker_NTR300_ch.get_tips(8)
            tip_eject(ham_int)

