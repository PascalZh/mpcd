from mpcd import PointCloud
import numpy as np

def demo_pcdtrans_concat():
    # pcd1
    pcd1 = PointCloud.from_path(
        "/Users/yuehao/Momenta/labeltest/sampled_data/436fcc645714492c68b42b5dd3ba80aa/1656923753.220280.360lidar.pcd"
    )
    # pcd2 with coor transformation
    pcd2 = PointCloud.from_path(
        "/Users/yuehao/Momenta/labeltest/sampled_data/436fcc645714492c68b42b5dd3ba80aa/1656923753.220280.360lidar.pcd"
    ).coor_trans(np.array([[1, 0, 0, 10], [0, 1, 0, 10], [0, 0, 1, 0], [0, 0, 0, 1]]))
    pcd3 = PointCloud.from_path(
        "/Users/yuehao/Momenta/labeltest/sampled_data/436fcc645714492c68b42b5dd3ba80aa/1656923753.220280.360lidar.pcd"
    ).coor_trans(np.array([[1, 0, 0, -10], [0, 1, 0, 10], [0, 0, 1, 0], [0, 0, 0, 1]]))
    # concat pcd1 and pcd2
    pcd_concat = PointCloud.pc_concat([pcd1, pcd2, pcd3])
    pcd_concat.save_pcd("pcd_concat.pcd")
    bev_concat = PointCloud.vis.draw_pc_overlay(((pcd1, "gray", 0), (pcd2, "cyan", 0)))


def demo_load_vis():
    pc_lidar = PointCloud.from_path('mpcd/test_data/9885806035_lidar.pcd')
    pc_radar = PointCloud.from_path('mpcd/test_data/9885806035_concat_radar.pcd')
    PointCloud.vis.draw_pc_overlay(((pc_lidar,'gray',0),(pc_radar,'cyan',1)))


if __name__ == "__main__":
    demo_load_vis()
    #demo_pcdtrans_concat()