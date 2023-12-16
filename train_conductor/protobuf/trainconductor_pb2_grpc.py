# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import trainconductor_pb2 as trainconductor__pb2


class TrainConductorStub(object):
    """-- SERVICES ----------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Train = channel.unary_unary(
                '/train_conductor.service.training.TrainConductor/Train',
                request_serializer=trainconductor__pb2.TrainingRequest.SerializeToString,
                response_deserializer=trainconductor__pb2.TrainingJob.FromString,
                )
        self.GetTrainingStatus = channel.unary_unary(
                '/train_conductor.service.training.TrainConductor/GetTrainingStatus',
                request_serializer=trainconductor__pb2.TrainingInfoRequest.SerializeToString,
                response_deserializer=trainconductor__pb2.TrainingStatusResponse.FromString,
                )
        self.CancelTraining = channel.unary_unary(
                '/train_conductor.service.training.TrainConductor/CancelTraining',
                request_serializer=trainconductor__pb2.TrainingInfoRequest.SerializeToString,
                response_deserializer=trainconductor__pb2.TrainingStatusResponse.FromString,
                )


class TrainConductorServicer(object):
    """-- SERVICES ----------------------------------------------------------------

    """

    def Train(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrainingStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelTraining(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainConductorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Train': grpc.unary_unary_rpc_method_handler(
                    servicer.Train,
                    request_deserializer=trainconductor__pb2.TrainingRequest.FromString,
                    response_serializer=trainconductor__pb2.TrainingJob.SerializeToString,
            ),
            'GetTrainingStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrainingStatus,
                    request_deserializer=trainconductor__pb2.TrainingInfoRequest.FromString,
                    response_serializer=trainconductor__pb2.TrainingStatusResponse.SerializeToString,
            ),
            'CancelTraining': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelTraining,
                    request_deserializer=trainconductor__pb2.TrainingInfoRequest.FromString,
                    response_serializer=trainconductor__pb2.TrainingStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'train_conductor.service.training.TrainConductor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrainConductor(object):
    """-- SERVICES ----------------------------------------------------------------

    """

    @staticmethod
    def Train(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/train_conductor.service.training.TrainConductor/Train',
            trainconductor__pb2.TrainingRequest.SerializeToString,
            trainconductor__pb2.TrainingJob.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrainingStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/train_conductor.service.training.TrainConductor/GetTrainingStatus',
            trainconductor__pb2.TrainingInfoRequest.SerializeToString,
            trainconductor__pb2.TrainingStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelTraining(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/train_conductor.service.training.TrainConductor/CancelTraining',
            trainconductor__pb2.TrainingInfoRequest.SerializeToString,
            trainconductor__pb2.TrainingStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)