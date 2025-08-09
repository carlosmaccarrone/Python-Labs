"""
OpenTelemetry is a set of tools, APIs, and SDKs for distributed telemetry. 
Its goal is to facilitate the collection of observability data such as traces, 
metrics, and logs in distributed applications and microservices.
"""
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.propagators.jaeger import JaegerPropagator
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.context import Context
from opentelemetry import propagate
from opentelemetry import trace, baggage
import os

class TracingService:
    """
    This is a wrapper/helper class to configure and use OpenTelemetry's tracing functionality,
    especially for exporting data to tools like Jaeger or standard formats.
    """
    def __init__(self, service_name_):
        self.service_name = service_name_

    def get_tracer(self):
        """ returns tracer object """
        return trace.get_tracer(self.service_name)

    def get_current_span(self, context: Context = None):
        """ return the current context """
        return trace.get_current_span(context)

    def set_tracer_provider(self, provider: TracerProvider):
        """ sets the traces tracer-provider """
        trace.set_tracer_provider(provider)

    def create_resource(self):
        """ creates a resource object and return it """
        return Resource.create( { SERVICE_NAME: self.service_name } )
    
    def create_tracer_provider(self, resource: Resource):
        """ creates a provider object and return it """
        return TracerProvider(resource=resource)
        
    def get_span_manager(self):
        """ creates a span manager property if it doesn't exist then returns the property """
        if not hasattr(TracingService, "span_manager"):
            self.span_manager = self.get_tracer().start_as_current_span(self.service_name)
        return self.span_manager

    def get_jaeger_exporter(self, host: str = "127.0.0.1", port: int = 8080):
        """ creates a jaeger exporter if doesn't exists then return it """
        if not hasattr(TracingService, "jaeger_exporter"):
            self.jaeger_exporter = JaegerExporter(agent_host_name=host, agent_port=port)
        return self.jaeger_exporter

    def get_OTLP_Span_Exporter(self, endpoint: str = "127.0.0.1:8080"):
        """ creates a jaeger exporter if doesn't exists then return it """
        if not hasattr(TracingService, "OTLP_Span_Exporter"):
            self.OTLP_Span_Exporter = OTLPSpanExporter(endpoint=endpoint)
        return self.OTLP_Span_Exporter

    def get_console_span_exporter(self):
        """ getter for simple console log exporter """
        if not hasattr(TracingService, "console_span_exporter"):
            self.console_span_exporter = ConsoleSpanExporter()
        return self.console_span_exporter 

    def get_batch_span_processor(self, exporter=None):
        """ creates a span processor if doesn't exists and return it """
        if not hasattr(TracingService, "batch_span_processor"):
            self.batch_span_processor = BatchSpanProcessor(exporter)
        return self.batch_span_processor

    def get_simple_span_processor(self, exporter):
        """ creates simple span processor if doesn't exists then return it """
        if not hasattr(TracingService, "simple_span_processor"):
            self.simple_span_processor = SimpleSpanProcessor(exporter)
        return self.simple_span_processor

    def get_textmap_propagator(self):
        """ getter for textmap propagator"""
        return propagate.get_global_textmap()

    def get_jaeger_propagator(self):
        """ creates jaeger propagator if doesn't exists the return it """
        if not hasattr(TracingService, "jaeger_propagator"):
            self.jaeger_propagator = JaegerPropagator()
        return self.jaeger_propagator

    def setUp(self):
        """ initiates all necessary instances to propagate the trace """
        resource = self.create_resource()
        host = os.getenv("JAEGER_AGENT_HOST")
        port = int(os.getenv("JAEGER_AGENT_PORT"))
        # endpoint = str(host) + ":" + str(port)
        exporter = self.get_jaeger_exporter(host, port)
        # exporter = self.get_OTLP_Span_Exporter(endpoint)
        provider = self.create_tracer_provider(resource)
        processor = self.get_batch_span_processor(exporter)
        provider.add_span_processor(processor)
        self.set_tracer_provider(provider)


#opentelemetry-api
#opentelemetry-sdk
#opentelemetry-instrumentation-fastapi
#opentelemetry-exporter-jaeger
#opentelemetry-exporter-otlp
#opentelemetry-propagator-gcp
#opentelemetry-propagator-jaeger
#opentelemetry-exporter-otlp-proto-grpc