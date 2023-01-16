from mpcd import PointCloud
import numpy as np

def demo_pcdtrans_concat(pcd_path1, pcd_path2, pcd_path3):
    # pcd123 should have the save filed name
    # pcd1
    pcd1 = PointCloud.from_path(pcd_path1)
    # pcd2 with coor transformation
    pcd2 = PointCloud.from_path(pcd_path2).coor_trans(np.array([[1, 0, 0, 10], [0, 1, 0, 10], [0, 0, 1, 0], [0, 0, 0, 1]]))
    # pcd3 with coor transformation
    pcd3 = PointCloud.from_path(pcd_path3).coor_trans(np.array([[1, 0, 0, -10], [0, 1, 0, 10], [0, 0, 1, 0], [0, 0, 0, 1]]))
    # concat a PointCloud list
    pcd_concat = PointCloud.pc_concat([pcd1, pcd2, pcd3])
    pcd_concat.save_pcd("pcd_concat.pcd")
    
def pcd_overlay_show(pcd_path1, pcd_path2):
    # pcd1
    pcd1 = PointCloud.from_path(pcd_path1)
    pcd2 = PointCloud.from_path(pcd_path2)
    PointCloud.vis.draw_pc_overlay(((pcd1,'gray',0),(pcd2,'cyan',1)))



if __name__ == "__main__":
    pass
    #pcd_overlay_show()
    #demo_pcdtrans_concat()