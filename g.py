#! /usr/bin/env python
# coding:utf-8

import os
import time
import pydicom


class G:
    def __init__(self, input_ds: pydicom.dataset.FileDataset, output_path):
        self._input_ds = input_ds
        self._output_ds = pydicom.dataset.FileDataset(
            os.path.basename(output_path), {},
            file_meta=self._gen_metadata(),
            preamble=b"\0" * 128)
        self._sop_instance_uid = pydicom.uid.generate_uid()

    def _gen_metadata(self):
        output_meta = pydicom.dataset.FileMetaDataset()
        input_meta = self._input_ds.file_meta
        output_meta.FileMetaInformationVersion = input_meta.FileMetaInformationVersion
        output_meta.MediaStorageSOPClassUID = "1.2.840.10008.5.1.4.1.1.11.1"
        output_meta.MediaStorageSOPInstanceUID = input_meta.MediaStorageSOPInstanceUID
        output_meta.TransferSyntaxUID = input_meta.TransferSyntaxUID
        output_meta.ImplementationClassUID = input_meta.ImplementationClassUID
        output_meta.ImplementationVersionName = input_meta.ImplementationVersionName
        return output_meta

    def _setup_for_gsps(self):
        self._output_ds.Modality = "PR"
        self._output_ds.InstanceCreationDate = time.strftime(
            "%Y%m%d", time.localtime(time.time()))
        self._output_ds.InstanceCreationTime = time.strftime(
            "%H%M%S", time.localtime(time.time()))

    def _copy_from_origin(self):
        data_elements = [
            "Patient ID", "Patient\'s Birth Date", "Study Instance UID",
            "Study Description", "Patient Name", "Patient Sex", "Study ID",
            "Study Date", "Study Time", "Referring Physician Name",
            "Accession Number", "Series Instance UID", "Manufacturer",
            "Specific Character Set"
        ]

        for de in input_dicom:
            if de.name in data_elements:
                dataset.add(de)
