# Copyright 2022 Open Reaction Database Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ord_schema/proto/dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ord_schema.proto import reaction_pb2 as ord__schema_dot_proto_dot_reaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eord_schema/proto/dataset.proto\x12\x03ord\x1a\x1ford_schema/proto/reaction.proto\"x\n\x07\x44\x61taset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12 \n\treactions\x18\x03 \x03(\x0b\x32\r.ord.Reaction\x12\x14\n\x0creaction_ids\x18\x04 \x03(\t\x12\x12\n\ndataset_id\x18\x05 \x01(\t\"i\n\x0e\x44\x61tasetExample\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12!\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x10.ord.RecordEventb\x06proto3')



_DATASET = DESCRIPTOR.message_types_by_name['Dataset']
_DATASETEXAMPLE = DESCRIPTOR.message_types_by_name['DatasetExample']
Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'ord_schema.proto.dataset_pb2'
  # @@protoc_insertion_point(class_scope:ord.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

DatasetExample = _reflection.GeneratedProtocolMessageType('DatasetExample', (_message.Message,), {
  'DESCRIPTOR' : _DATASETEXAMPLE,
  '__module__' : 'ord_schema.proto.dataset_pb2'
  # @@protoc_insertion_point(class_scope:ord.DatasetExample)
  })
_sym_db.RegisterMessage(DatasetExample)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATASET._serialized_start=72
  _DATASET._serialized_end=192
  _DATASETEXAMPLE._serialized_start=194
  _DATASETEXAMPLE._serialized_end=299
# @@protoc_insertion_point(module_scope)
