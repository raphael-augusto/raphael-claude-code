"""
Structured logging template para pipelines
"""
import logging
import json
from datetime import datetime
from typing import Dict, Any

class StructuredLogger:
    def __init__(self, pipeline_name: str, environment: str = "prod"):
        self.pipeline_name = pipeline_name
        self.environment = environment
        self.logger = logging.getLogger(pipeline_name)
        self.logger.setLevel(logging.INFO)

        # JSON formatter
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)

    def _build_log(self, level: str, message: str, **kwargs: Any) -> Dict:
        return {
            'timestamp': datetime.utcnow().isoformat(),
            'level': level,
            'pipeline_name': self.pipeline_name,
            'environment': self.environment,
            'message': message,
            **kwargs
        }

    def info(self, message: str, **kwargs):
        self.logger.info(json.dumps(self._build_log('INFO', message, **kwargs)))

    def warning(self, message: str, **kwargs):
        self.logger.warning(json.dumps(self._build_log('WARNING', message, **kwargs)))

    def error(self, message: str, **kwargs):
        self.logger.error(json.dumps(self._build_log('ERROR', message, **kwargs)))

# Usage
logger = StructuredLogger(pipeline_name="bronze_to_silver", environment="prod")

logger.info("Pipeline started",
            source_table="bronze.orders",
            target_table="silver.orders",
            partition_date="2024-01-01")

logger.info("Records processed",
            total_records=10000,
            failed_records=5,
            duration_seconds=120.5)

logger.error("Data quality check failed",
             check_name="null_business_key",
             failed_count=10,
             threshold=0)
