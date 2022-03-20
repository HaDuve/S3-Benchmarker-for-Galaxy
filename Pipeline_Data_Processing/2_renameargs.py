with open("nh.csv", "r") as f:
    lines = f.readlines()
with open("nhf.csv", "w") as f:
    headerline = True
    for line in lines:
        if (headerline):
            headerline=False

            # change headers
            line = line.replace("Argument1","Filetype")
            line = line.replace("Argument2","Filesize")
            line = line.replace(", Argument3","")
            f.write(line)
            continue
        # strip ,None
        # change filepaths to respective type + size

        #hdf5 small
        line = line.replace("/mnt/Benchfiles/Data/HDF5/np_rx_ofdm_entries.hdf5,None,None","HDF5, small")
        line = line.replace("Benchfiles/Data/HDF5/np_rx_ofdm_entries.hdf5,None,None","HDF5, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/HDF5/np_rx_ofdm_entries.hdf5,/mnt/Benchfiles/Data/HDF5/np_rx_ofdm_entries.hdf5,None","HDF5, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/HDF5/np_rx_ofdm_entries.hdf5,/Benchfiles/Data/HDF5,None","HDF5, small")
        #hdf5 medium
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/HDF5/ap_one_node_capture.hdf5,/mnt/Benchfiles/Data/HDF5/ap_one_node_capture.hdf5,None","HDF5, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/HDF5/ap_one_node_capture.hdf5,/Benchfiles/Data/HDF5,None","HDF5, medium")
        line = line.replace("/mnt/Benchfiles/Data/HDF5/ap_one_node_capture.hdf5,None,None","HDF5, medium")
        line = line.replace("Benchfiles/Data/HDF5/ap_one_node_capture.hdf5,None,None","HDF5, medium")
        #hdf5 big
        line = line.replace("/mnt/Benchfiles/Data/HDF5/ap_two_node_two_flow_capture.hdf5,None,None","HDF5, big")
        line = line.replace("Benchfiles/Data/HDF5/ap_two_node_two_flow_capture.hdf5,None,None","HDF5, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/HDF5/ap_two_node_two_flow_capture.hdf5,/mnt/Benchfiles/Data/HDF5/ap_two_node_two_flow_capture.hdf5,None","HDF5, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/HDF5/ap_two_node_two_flow_capture.hdf5,/Benchfiles/Data/HDF5,None","HDF5, big")

        #JPG small
        line = line.replace("/mnt/Benchfiles/Data/JPG/file_example_JPG_100kB.jpg,None,None","JPG, small")
        line = line.replace("Benchfiles/Data/JPG/file_example_JPG_100kB.jpg,None,None","JPG, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/JPG/file_example_JPG_100kB.jpg,/mnt/Benchfiles/Data/JPG/file_example_JPG_100kB.jpg,None","JPG, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/JPG/file_example_JPG_100kB.jpg,/Benchfiles/Data/JPG,None","JPG, small")
        #JPG medium
        line = line.replace("/mnt/Benchfiles/Data/JPG/file_example_JPG_1MB.jpg,None,None","JPG, medium")
        line = line.replace("Benchfiles/Data/JPG/file_example_JPG_1MB.jpg,None,None","JPG, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/JPG/file_example_JPG_1MB.jpg,/mnt/Benchfiles/Data/JPG/file_example_JPG_1MB.jpg,None","JPG, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/JPG/file_example_JPG_1MB.jpg,/Benchfiles/Data/JPG,None","JPG, medium")
        #JPG big
        line = line.replace("/mnt/Benchfiles/Data/JPG/file_example_JPG_2500kB.jpg,None,None","JPG, big")
        line = line.replace("Benchfiles/Data/JPG/file_example_JPG_2500kB.jpg,None,None","JPG, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/JPG/file_example_JPG_2500kB.jpg,/mnt/Benchfiles/Data/JPG/file_example_JPG_2500kB.jpg,None","JPG, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/JPG/file_example_JPG_2500kB.jpg,/Benchfiles/Data/JPG,None","JPG, big")

        # MP4 small
        line = line.replace("/mnt/Benchfiles/Data/MP4/SampleVideo_1280x720_1mb.mp4,None,None","MP4, small")
        line = line.replace("Benchfiles/Data/MP4/SampleVideo_1280x720_1mb.mp4,None,None","MP4, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/MP4/SampleVideo_1280x720_1mb.mp4,/mnt/Benchfiles/Data/MP4/SampleVideo_1280x720_1mb.mp4,None","MP4, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/MP4/SampleVideo_1280x720_1mb.mp4,/Benchfiles/Data/MP4,None","MP4, small")
        # MP4 medium
        line = line.replace("/mnt/Benchfiles/Data/MP4/SampleVideo_1280x720_5mb.mp4,None,None","MP4, medium")
        line = line.replace("Benchfiles/Data/MP4/SampleVideo_1280x720_5mb.mp4,None,None","MP4, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/MP4/SampleVideo_1280x720_5mb.mp4,/mnt/Benchfiles/Data/MP4/SampleVideo_1280x720_5mb.mp4,None","MP4, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/MP4/SampleVideo_1280x720_5mb.mp4,/Benchfiles/Data/MP4,None","MP4, medium")
        # MP4 big
        line = line.replace("/mnt/Benchfiles/Data/MP4/SampleVideo_1280x720_30mb.mp4,None,None","MP4, big")
        line = line.replace("Benchfiles/Data/MP4/SampleVideo_1280x720_30mb.mp4,None,None","MP4, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/MP4/SampleVideo_1280x720_30mb.mp4,/mnt/Benchfiles/Data/MP4/SampleVideo_1280x720_30mb.mp4,None","MP4, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/MP4/SampleVideo_1280x720_30mb.mp4,/Benchfiles/Data/MP4,None","MP4, big")

        # NetCDF small
        line = line.replace("/mnt/Benchfiles/Data/NetCDF/sresa1b_ncar_ccsm3-example.nc,None,None","NetCDF, small")
        line = line.replace("Benchfiles/Data/NetCDF/sresa1b_ncar_ccsm3-example.nc,None,None","NetCDF, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/NetCDF/sresa1b_ncar_ccsm3-example.nc,/mnt/Benchfiles/Data/NetCDF/sresa1b_ncar_ccsm3-example.nc,None","NetCDF, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/NetCDF/sresa1b_ncar_ccsm3-example.nc,/Benchfiles/Data/NetCDF,None","NetCDF, small")
        # NetCDF medium
        line = line.replace("/mnt/Benchfiles/Data/NetCDF/ECMWF_ERA-40_subset.nc,None,None","NetCDF, medium")
        line = line.replace("Benchfiles/Data/NetCDF/ECMWF_ERA-40_subset.nc,None,None","NetCDF, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/NetCDF/ECMWF_ERA-40_subset.nc,/mnt/Benchfiles/Data/NetCDF/ECMWF_ERA-40_subset.nc,None","NetCDF, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/NetCDF/ECMWF_ERA-40_subset.nc,/Benchfiles/Data/NetCDF,None","NetCDF, medium")
        # NetCDF big
        line = line.replace("/mnt/Benchfiles/Data/NetCDF/test_echam_spectral.nc,None,None","NetCDF, big")
        line = line.replace("Benchfiles/Data/NetCDF/test_echam_spectral.nc,None,None","NetCDF, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/NetCDF/test_echam_spectral.nc,/mnt/Benchfiles/Data/NetCDF/test_echam_spectral.nc,None","NetCDF, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/NetCDF/test_echam_spectral.nc,/Benchfiles/Data/NetCDF,None","NetCDF, big")

        # fasta small
        line = line.replace("/mnt/Benchfiles/Data/FASTA/rcsb_pdb_4Q4W.fasta,None,None","FASTA, small")
        line = line.replace("Benchfiles/Data/FASTA/rcsb_pdb_4Q4W.fasta,None,None","FASTA, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTA/rcsb_pdb_4Q4W.fasta,/mnt/Benchfiles/Data/FASTA/rcsb_pdb_4Q4W.fasta,None","FASTA, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTA/rcsb_pdb_4Q4W.fasta,/Benchfiles/Data/FASTA,None","FASTA, small")

        # fasta big
        line = line.replace("/mnt/Benchfiles/Data/FASTA/hg19.fa.gz,None,None","FASTA, big")
        line = line.replace("Benchfiles/Data/FASTA/hg19.fa.gz,None,None","FASTA, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTA/hg19.fa.gz,/mnt/Benchfiles/Data/FASTA/hg19.fa.gz,None","FASTA, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTA/hg19.fa.gz,/Benchfiles/Data/FASTA,None","FASTA, big")


        # fastq small
        line = line.replace("/mnt/Benchfiles/Data/FASTQ/1_control_psbA3_2019_minq7.fastq,None,None","FASTQ, small")
        line = line.replace("Benchfiles/Data/FASTQ/1_control_psbA3_2019_minq7.fastq,None,None","FASTQ, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTQ/1_control_psbA3_2019_minq7.fastq,/mnt/Benchfiles/Data/FASTQ/1_control_psbA3_2019_minq7.fastq,None","FASTQ, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTQ/1_control_psbA3_2019_minq7.fastq,/Benchfiles/Data/FASTQ,None","FASTQ, small")
        # fastq medium
        line = line.replace("/mnt/Benchfiles/Data/FASTQ/1_control_18S_2019_minq7.fastq,None,None","FASTQ, medium")
        line = line.replace("Benchfiles/Data/FASTQ/1_control_18S_2019_minq7.fastq,None,None","FASTQ, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTQ/1_control_18S_2019_minq7.fastq,/mnt/Benchfiles/Data/FASTQ/1_control_18S_2019_minq7.fastq,None","FASTQ, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTQ/1_control_18S_2019_minq7.fastq,/Benchfiles/Data/FASTQ,None","FASTQ, medium")
        # fastq big
        line = line.replace("/mnt/Benchfiles/Data/FASTQ/9_Swamp_S2B_rbcLa_2019_minq7.fastq,None,None","FASTQ, big")
        line = line.replace("Benchfiles/Data/FASTQ/9_Swamp_S2B_rbcLa_2019_minq7.fastq,None,None","FASTQ, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTQ/9_Swamp_S2B_rbcLa_2019_minq7.fastq,/mnt/Benchfiles/Data/FASTQ/9_Swamp_S2B_rbcLa_2019_minq7.fastq,None","FASTQ, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/FASTQ/9_Swamp_S2B_rbcLa_2019_minq7.fastq,/Benchfiles/Data/FASTQ,None","FASTQ, big")

        # gzip small
        line = line.replace("/mnt/Benchfiles/Data/gzip/constitution.txt.gz,None,None","gzip, small")
        line = line.replace("Benchfiles/Data/gzip/constitution.txt.gz,None,None","gzip, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/gzip/constitution.txt.gz,/mnt/Benchfiles/Data/gzip/gzip/constitution.txt.gz,None","gzip, small")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/gzip/constitution.txt.gz,/Benchfiles/Data/gzip,None","gzip, small")
        # gzip medium
        line = line.replace("/mnt/Benchfiles/Data/gzip/External_test_data.tar.gz,None,None","gzip, medium")
        line = line.replace("Benchfiles/Data/gzip/External_test_data.tar.gz,None,None","gzip, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/gzip/External_test_data.tar.gz,/mnt/Benchfiles/Data/gzip/gzip/External_test_data.tar.gz,None","gzip, medium")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/gzip/External_test_data.tar.gz,/Benchfiles/Data/gzip,None","gzip, medium")
        # gzip big
        line = line.replace("/mnt/Benchfiles/Data/gzip/pxproteome.tar.gz,None,None","gzip, big")
        line = line.replace("Benchfiles/Data/gzip/pxproteome.tar.gz,None,None","gzip, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/gzip/pxproteome.tar.gz,/mnt/Benchfiles/Data/gzip/pxproteome.tar.gz,None","gzip, big")
        line = line.replace("/git/S3-Benchmarker-for-Galaxy/Database/Benchfiles/gzip/pxproteome.tar.gz,/Benchfiles/Data/gzip,None","gzip, big")

        f.write(line)
