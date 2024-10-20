from typing import ClassVar

from . import _base
from ._base import *

class PostgresWarning(_base.PostgresLogMessage, Warning):
    sqlstate: ClassVar[str]

class DynamicResultSetsReturned(PostgresWarning):
    sqlstate: ClassVar[str]

class ImplicitZeroBitPadding(PostgresWarning):
    sqlstate: ClassVar[str]

class NullValueEliminatedInSetFunction(PostgresWarning):
    sqlstate: ClassVar[str]

class PrivilegeNotGranted(PostgresWarning):
    sqlstate: ClassVar[str]

class PrivilegeNotRevoked(PostgresWarning):
    sqlstate: ClassVar[str]

class StringDataRightTruncation(PostgresWarning):
    sqlstate: ClassVar[str]

class DeprecatedFeature(PostgresWarning):
    sqlstate: ClassVar[str]

class NoData(PostgresWarning):
    sqlstate: ClassVar[str]

class NoAdditionalDynamicResultSetsReturned(NoData):
    sqlstate: ClassVar[str]

class SQLStatementNotYetCompleteError(_base.PostgresError):
    sqlstate: ClassVar[str]

class PostgresConnectionError(_base.PostgresError):
    sqlstate: ClassVar[str]

class ConnectionDoesNotExistError(PostgresConnectionError):
    sqlstate: ClassVar[str]

class ConnectionFailureError(PostgresConnectionError):
    sqlstate: ClassVar[str]

class ClientCannotConnectError(PostgresConnectionError):
    sqlstate: ClassVar[str]

class ConnectionRejectionError(PostgresConnectionError):
    sqlstate: ClassVar[str]

class TransactionResolutionUnknownError(PostgresConnectionError):
    sqlstate: ClassVar[str]

class ProtocolViolationError(PostgresConnectionError):
    sqlstate: ClassVar[str]

class TriggeredActionError(_base.PostgresError):
    sqlstate: ClassVar[str]

class FeatureNotSupportedError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidCachedStatementError(FeatureNotSupportedError): ...

class InvalidTransactionInitiationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class LocatorError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidLocatorSpecificationError(LocatorError):
    sqlstate: ClassVar[str]

class InvalidGrantorError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidGrantOperationError(InvalidGrantorError):
    sqlstate: ClassVar[str]

class InvalidRoleSpecificationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class DiagnosticsError(_base.PostgresError):
    sqlstate: ClassVar[str]

class StackedDiagnosticsAccessedWithoutActiveHandlerError(DiagnosticsError):
    sqlstate: ClassVar[str]

class InvalidArgumentForXqueryError(_base.PostgresError):
    sqlstate: ClassVar[str]

class CaseNotFoundError(_base.PostgresError):
    sqlstate: ClassVar[str]

class CardinalityViolationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class DataError(_base.PostgresError):
    sqlstate: ClassVar[str]

class ArraySubscriptError(DataError):
    sqlstate: ClassVar[str]

class CharacterNotInRepertoireError(DataError):
    sqlstate: ClassVar[str]

class DatetimeFieldOverflowError(DataError):
    sqlstate: ClassVar[str]

class DivisionByZeroError(DataError):
    sqlstate: ClassVar[str]

class ErrorInAssignmentError(DataError):
    sqlstate: ClassVar[str]

class EscapeCharacterConflictError(DataError):
    sqlstate: ClassVar[str]

class IndicatorOverflowError(DataError):
    sqlstate: ClassVar[str]

class IntervalFieldOverflowError(DataError):
    sqlstate: ClassVar[str]

class InvalidArgumentForLogarithmError(DataError):
    sqlstate: ClassVar[str]

class InvalidArgumentForNtileFunctionError(DataError):
    sqlstate: ClassVar[str]

class InvalidArgumentForNthValueFunctionError(DataError):
    sqlstate: ClassVar[str]

class InvalidArgumentForPowerFunctionError(DataError):
    sqlstate: ClassVar[str]

class InvalidArgumentForWidthBucketFunctionError(DataError):
    sqlstate: ClassVar[str]

class InvalidCharacterValueForCastError(DataError):
    sqlstate: ClassVar[str]

class InvalidDatetimeFormatError(DataError):
    sqlstate: ClassVar[str]

class InvalidEscapeCharacterError(DataError):
    sqlstate: ClassVar[str]

class InvalidEscapeOctetError(DataError):
    sqlstate: ClassVar[str]

class InvalidEscapeSequenceError(DataError):
    sqlstate: ClassVar[str]

class NonstandardUseOfEscapeCharacterError(DataError):
    sqlstate: ClassVar[str]

class InvalidIndicatorParameterValueError(DataError):
    sqlstate: ClassVar[str]

class InvalidParameterValueError(DataError):
    sqlstate: ClassVar[str]

class InvalidPrecedingOrFollowingSizeError(DataError):
    sqlstate: ClassVar[str]

class InvalidRegularExpressionError(DataError):
    sqlstate: ClassVar[str]

class InvalidRowCountInLimitClauseError(DataError):
    sqlstate: ClassVar[str]

class InvalidRowCountInResultOffsetClauseError(DataError):
    sqlstate: ClassVar[str]

class InvalidTablesampleArgumentError(DataError):
    sqlstate: ClassVar[str]

class InvalidTablesampleRepeatError(DataError):
    sqlstate: ClassVar[str]

class InvalidTimeZoneDisplacementValueError(DataError):
    sqlstate: ClassVar[str]

class InvalidUseOfEscapeCharacterError(DataError):
    sqlstate: ClassVar[str]

class MostSpecificTypeMismatchError(DataError):
    sqlstate: ClassVar[str]

class NullValueNotAllowedError(DataError):
    sqlstate: ClassVar[str]

class NullValueNoIndicatorParameterError(DataError):
    sqlstate: ClassVar[str]

class NumericValueOutOfRangeError(DataError):
    sqlstate: ClassVar[str]

class SequenceGeneratorLimitExceededError(DataError):
    sqlstate: ClassVar[str]

class StringDataLengthMismatchError(DataError):
    sqlstate: ClassVar[str]

class StringDataRightTruncationError(DataError):
    sqlstate: ClassVar[str]

class SubstringError(DataError):
    sqlstate: ClassVar[str]

class TrimError(DataError):
    sqlstate: ClassVar[str]

class UnterminatedCStringError(DataError):
    sqlstate: ClassVar[str]

class ZeroLengthCharacterStringError(DataError):
    sqlstate: ClassVar[str]

class PostgresFloatingPointError(DataError):
    sqlstate: ClassVar[str]

class InvalidTextRepresentationError(DataError):
    sqlstate: ClassVar[str]

class InvalidBinaryRepresentationError(DataError):
    sqlstate: ClassVar[str]

class BadCopyFileFormatError(DataError):
    sqlstate: ClassVar[str]

class UntranslatableCharacterError(DataError):
    sqlstate: ClassVar[str]

class NotAnXmlDocumentError(DataError):
    sqlstate: ClassVar[str]

class InvalidXmlDocumentError(DataError):
    sqlstate: ClassVar[str]

class InvalidXmlContentError(DataError):
    sqlstate: ClassVar[str]

class InvalidXmlCommentError(DataError):
    sqlstate: ClassVar[str]

class InvalidXmlProcessingInstructionError(DataError):
    sqlstate: ClassVar[str]

class DuplicateJsonObjectKeyValueError(DataError):
    sqlstate: ClassVar[str]

class InvalidArgumentForSQLJsonDatetimeFunctionError(DataError):
    sqlstate: ClassVar[str]

class InvalidJsonTextError(DataError):
    sqlstate: ClassVar[str]

class InvalidSQLJsonSubscriptError(DataError):
    sqlstate: ClassVar[str]

class MoreThanOneSQLJsonItemError(DataError):
    sqlstate: ClassVar[str]

class NoSQLJsonItemError(DataError):
    sqlstate: ClassVar[str]

class NonNumericSQLJsonItemError(DataError):
    sqlstate: ClassVar[str]

class NonUniqueKeysInAJsonObjectError(DataError):
    sqlstate: ClassVar[str]

class SingletonSQLJsonItemRequiredError(DataError):
    sqlstate: ClassVar[str]

class SQLJsonArrayNotFoundError(DataError):
    sqlstate: ClassVar[str]

class SQLJsonMemberNotFoundError(DataError):
    sqlstate: ClassVar[str]

class SQLJsonNumberNotFoundError(DataError):
    sqlstate: ClassVar[str]

class SQLJsonObjectNotFoundError(DataError):
    sqlstate: ClassVar[str]

class TooManyJsonArrayElementsError(DataError):
    sqlstate: ClassVar[str]

class TooManyJsonObjectMembersError(DataError):
    sqlstate: ClassVar[str]

class SQLJsonScalarRequiredError(DataError):
    sqlstate: ClassVar[str]

class SQLJsonItemCannotBeCastToTargetTypeError(DataError):
    sqlstate: ClassVar[str]

class IntegrityConstraintViolationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class RestrictViolationError(IntegrityConstraintViolationError):
    sqlstate: ClassVar[str]

class NotNullViolationError(IntegrityConstraintViolationError):
    sqlstate: ClassVar[str]

class ForeignKeyViolationError(IntegrityConstraintViolationError):
    sqlstate: ClassVar[str]

class UniqueViolationError(IntegrityConstraintViolationError):
    sqlstate: ClassVar[str]

class CheckViolationError(IntegrityConstraintViolationError):
    sqlstate: ClassVar[str]

class ExclusionViolationError(IntegrityConstraintViolationError):
    sqlstate: ClassVar[str]

class InvalidCursorStateError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidTransactionStateError(_base.PostgresError):
    sqlstate: ClassVar[str]

class ActiveSQLTransactionError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class BranchTransactionAlreadyActiveError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class HeldCursorRequiresSameIsolationLevelError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class InappropriateAccessModeForBranchTransactionError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class InappropriateIsolationLevelForBranchTransactionError(
    InvalidTransactionStateError
):
    sqlstate: ClassVar[str]

class NoActiveSQLTransactionForBranchTransactionError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class ReadOnlySQLTransactionError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class SchemaAndDataStatementMixingNotSupportedError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class NoActiveSQLTransactionError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class InFailedSQLTransactionError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class IdleInTransactionSessionTimeoutError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class TransactionTimeoutError(InvalidTransactionStateError):
    sqlstate: ClassVar[str]

class InvalidSQLStatementNameError(_base.PostgresError):
    sqlstate: ClassVar[str]

class TriggeredDataChangeViolationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidAuthorizationSpecificationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidPasswordError(InvalidAuthorizationSpecificationError):
    sqlstate: ClassVar[str]

class DependentPrivilegeDescriptorsStillExistError(_base.PostgresError):
    sqlstate: ClassVar[str]

class DependentObjectsStillExistError(DependentPrivilegeDescriptorsStillExistError):
    sqlstate: ClassVar[str]

class InvalidTransactionTerminationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class SQLRoutineError(_base.PostgresError):
    sqlstate: ClassVar[str]

class FunctionExecutedNoReturnStatementError(SQLRoutineError):
    sqlstate: ClassVar[str]

class ModifyingSQLDataNotPermittedError(SQLRoutineError):
    sqlstate: ClassVar[str]

class ProhibitedSQLStatementAttemptedError(SQLRoutineError):
    sqlstate: ClassVar[str]

class ReadingSQLDataNotPermittedError(SQLRoutineError):
    sqlstate: ClassVar[str]

class InvalidCursorNameError(_base.PostgresError):
    sqlstate: ClassVar[str]

class ExternalRoutineError(_base.PostgresError):
    sqlstate: ClassVar[str]

class ContainingSQLNotPermittedError(ExternalRoutineError):
    sqlstate: ClassVar[str]

class ModifyingExternalRoutineSQLDataNotPermittedError(ExternalRoutineError):
    sqlstate: ClassVar[str]

class ProhibitedExternalRoutineSQLStatementAttemptedError(ExternalRoutineError):
    sqlstate: ClassVar[str]

class ReadingExternalRoutineSQLDataNotPermittedError(ExternalRoutineError):
    sqlstate: ClassVar[str]

class ExternalRoutineInvocationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidSqlstateReturnedError(ExternalRoutineInvocationError):
    sqlstate: ClassVar[str]

class NullValueInExternalRoutineNotAllowedError(ExternalRoutineInvocationError):
    sqlstate: ClassVar[str]

class TriggerProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: ClassVar[str]

class SrfProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: ClassVar[str]

class EventTriggerProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: ClassVar[str]

class SavepointError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidSavepointSpecificationError(SavepointError):
    sqlstate: ClassVar[str]

class InvalidCatalogNameError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InvalidSchemaNameError(_base.PostgresError):
    sqlstate: ClassVar[str]

class TransactionRollbackError(_base.PostgresError):
    sqlstate: ClassVar[str]

class TransactionIntegrityConstraintViolationError(TransactionRollbackError):
    sqlstate: ClassVar[str]

class SerializationError(TransactionRollbackError):
    sqlstate: ClassVar[str]

class StatementCompletionUnknownError(TransactionRollbackError):
    sqlstate: ClassVar[str]

class DeadlockDetectedError(TransactionRollbackError):
    sqlstate: ClassVar[str]

class SyntaxOrAccessError(_base.PostgresError):
    sqlstate: ClassVar[str]

class PostgresSyntaxError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InsufficientPrivilegeError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class CannotCoerceError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class GroupingError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class WindowingError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidRecursionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidForeignKeyError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidNameError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class NameTooLongError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class ReservedNameError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DatatypeMismatchError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class IndeterminateDatatypeError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class CollationMismatchError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class IndeterminateCollationError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class WrongObjectTypeError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class GeneratedAlwaysError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class UndefinedColumnError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class UndefinedFunctionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class UndefinedTableError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class UndefinedParameterError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class UndefinedObjectError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateColumnError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateCursorError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateDatabaseError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateFunctionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicatePreparedStatementError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateSchemaError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateTableError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateAliasError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class DuplicateObjectError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class AmbiguousColumnError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class AmbiguousFunctionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class AmbiguousParameterError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class AmbiguousAliasError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidColumnReferenceError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidColumnDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidCursorDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidDatabaseDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidFunctionDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidPreparedStatementDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidSchemaDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidTableDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class InvalidObjectDefinitionError(SyntaxOrAccessError):
    sqlstate: ClassVar[str]

class WithCheckOptionViolationError(_base.PostgresError):
    sqlstate: ClassVar[str]

class InsufficientResourcesError(_base.PostgresError):
    sqlstate: ClassVar[str]

class DiskFullError(InsufficientResourcesError):
    sqlstate: ClassVar[str]

class OutOfMemoryError(InsufficientResourcesError):
    sqlstate: ClassVar[str]

class TooManyConnectionsError(InsufficientResourcesError):
    sqlstate: ClassVar[str]

class ConfigurationLimitExceededError(InsufficientResourcesError):
    sqlstate: ClassVar[str]

class ProgramLimitExceededError(_base.PostgresError):
    sqlstate: ClassVar[str]

class StatementTooComplexError(ProgramLimitExceededError):
    sqlstate: ClassVar[str]

class TooManyColumnsError(ProgramLimitExceededError):
    sqlstate: ClassVar[str]

class TooManyArgumentsError(ProgramLimitExceededError):
    sqlstate: ClassVar[str]

class ObjectNotInPrerequisiteStateError(_base.PostgresError):
    sqlstate: ClassVar[str]

class ObjectInUseError(ObjectNotInPrerequisiteStateError):
    sqlstate: ClassVar[str]

class CantChangeRuntimeParamError(ObjectNotInPrerequisiteStateError):
    sqlstate: ClassVar[str]

class LockNotAvailableError(ObjectNotInPrerequisiteStateError):
    sqlstate: ClassVar[str]

class UnsafeNewEnumValueUsageError(ObjectNotInPrerequisiteStateError):
    sqlstate: ClassVar[str]

class OperatorInterventionError(_base.PostgresError):
    sqlstate: ClassVar[str]

class QueryCanceledError(OperatorInterventionError):
    sqlstate: ClassVar[str]

class AdminShutdownError(OperatorInterventionError):
    sqlstate: ClassVar[str]

class CrashShutdownError(OperatorInterventionError):
    sqlstate: ClassVar[str]

class CannotConnectNowError(OperatorInterventionError):
    sqlstate: ClassVar[str]

class DatabaseDroppedError(OperatorInterventionError):
    sqlstate: ClassVar[str]

class IdleSessionTimeoutError(OperatorInterventionError):
    sqlstate: ClassVar[str]

class PostgresSystemError(_base.PostgresError):
    sqlstate: ClassVar[str]

class PostgresIOError(PostgresSystemError):
    sqlstate: ClassVar[str]

class UndefinedFileError(PostgresSystemError):
    sqlstate: ClassVar[str]

class DuplicateFileError(PostgresSystemError):
    sqlstate: ClassVar[str]

class FileNameTooLongError(PostgresSystemError):
    sqlstate: ClassVar[str]

class SnapshotTooOldError(_base.PostgresError):
    sqlstate: ClassVar[str]

class ConfigFileError(_base.PostgresError):
    sqlstate: ClassVar[str]

class LockFileExistsError(ConfigFileError):
    sqlstate: ClassVar[str]

class FDWError(_base.PostgresError):
    sqlstate: ClassVar[str]

class FDWColumnNameNotFoundError(FDWError):
    sqlstate: ClassVar[str]

class FDWDynamicParameterValueNeededError(FDWError):
    sqlstate: ClassVar[str]

class FDWFunctionSequenceError(FDWError):
    sqlstate: ClassVar[str]

class FDWInconsistentDescriptorInformationError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidAttributeValueError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidColumnNameError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidColumnNumberError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidDataTypeError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidDataTypeDescriptorsError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidDescriptorFieldIdentifierError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidHandleError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidOptionIndexError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidOptionNameError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidStringLengthOrBufferLengthError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidStringFormatError(FDWError):
    sqlstate: ClassVar[str]

class FDWInvalidUseOfNullPointerError(FDWError):
    sqlstate: ClassVar[str]

class FDWTooManyHandlesError(FDWError):
    sqlstate: ClassVar[str]

class FDWOutOfMemoryError(FDWError):
    sqlstate: ClassVar[str]

class FDWNoSchemasError(FDWError):
    sqlstate: ClassVar[str]

class FDWOptionNameNotFoundError(FDWError):
    sqlstate: ClassVar[str]

class FDWReplyHandleError(FDWError):
    sqlstate: ClassVar[str]

class FDWSchemaNotFoundError(FDWError):
    sqlstate: ClassVar[str]

class FDWTableNotFoundError(FDWError):
    sqlstate: ClassVar[str]

class FDWUnableToCreateExecutionError(FDWError):
    sqlstate: ClassVar[str]

class FDWUnableToCreateReplyError(FDWError):
    sqlstate: ClassVar[str]

class FDWUnableToEstablishConnectionError(FDWError):
    sqlstate: ClassVar[str]

class PLPGSQLError(_base.PostgresError):
    sqlstate: ClassVar[str]

class RaiseError(PLPGSQLError):
    sqlstate: ClassVar[str]

class NoDataFoundError(PLPGSQLError):
    sqlstate: ClassVar[str]

class TooManyRowsError(PLPGSQLError):
    sqlstate: ClassVar[str]

class AssertError(PLPGSQLError):
    sqlstate: ClassVar[str]

class InternalServerError(_base.PostgresError):
    sqlstate: ClassVar[str]

class DataCorruptedError(InternalServerError):
    sqlstate: ClassVar[str]

class IndexCorruptedError(InternalServerError):
    sqlstate: ClassVar[str]

__all__: tuple[str, ...] = (
    # From _base.pyi
    'PostgresError',
    'FatalPostgresError',
    'UnknownPostgresError',
    'InterfaceError',
    'InterfaceWarning',
    'PostgresLogMessage',
    'ClientConfigurationError',
    'InternalClientError',
    'OutdatedSchemaCacheError',
    'ProtocolError',
    'UnsupportedClientFeatureError',
    'TargetServerAttributeNotMatched',
    'UnsupportedServerFeatureError',
    # End from _base.pyi
    'ActiveSQLTransactionError',
    'AdminShutdownError',
    'AmbiguousAliasError',
    'AmbiguousColumnError',
    'AmbiguousFunctionError',
    'AmbiguousParameterError',
    'ArraySubscriptError',
    'AssertError',
    'BadCopyFileFormatError',
    'BranchTransactionAlreadyActiveError',
    'CannotCoerceError',
    'CannotConnectNowError',
    'CantChangeRuntimeParamError',
    'CardinalityViolationError',
    'CaseNotFoundError',
    'CharacterNotInRepertoireError',
    'CheckViolationError',
    'ClientCannotConnectError',
    'CollationMismatchError',
    'ConfigFileError',
    'ConfigurationLimitExceededError',
    'ConnectionDoesNotExistError',
    'ConnectionFailureError',
    'ConnectionRejectionError',
    'ContainingSQLNotPermittedError',
    'CrashShutdownError',
    'DataCorruptedError',
    'DataError',
    'DatabaseDroppedError',
    'DatatypeMismatchError',
    'DatetimeFieldOverflowError',
    'DeadlockDetectedError',
    'DependentObjectsStillExistError',
    'DependentPrivilegeDescriptorsStillExistError',
    'DeprecatedFeature',
    'DiagnosticsError',
    'DiskFullError',
    'DivisionByZeroError',
    'DuplicateAliasError',
    'DuplicateColumnError',
    'DuplicateCursorError',
    'DuplicateDatabaseError',
    'DuplicateFileError',
    'DuplicateFunctionError',
    'DuplicateJsonObjectKeyValueError',
    'DuplicateObjectError',
    'DuplicatePreparedStatementError',
    'DuplicateSchemaError',
    'DuplicateTableError',
    'DynamicResultSetsReturned',
    'ErrorInAssignmentError',
    'EscapeCharacterConflictError',
    'EventTriggerProtocolViolatedError',
    'ExclusionViolationError',
    'ExternalRoutineError',
    'ExternalRoutineInvocationError',
    'FDWColumnNameNotFoundError',
    'FDWDynamicParameterValueNeededError',
    'FDWError',
    'FDWFunctionSequenceError',
    'FDWInconsistentDescriptorInformationError',
    'FDWInvalidAttributeValueError',
    'FDWInvalidColumnNameError',
    'FDWInvalidColumnNumberError',
    'FDWInvalidDataTypeDescriptorsError',
    'FDWInvalidDataTypeError',
    'FDWInvalidDescriptorFieldIdentifierError',
    'FDWInvalidHandleError',
    'FDWInvalidOptionIndexError',
    'FDWInvalidOptionNameError',
    'FDWInvalidStringFormatError',
    'FDWInvalidStringLengthOrBufferLengthError',
    'FDWInvalidUseOfNullPointerError',
    'FDWNoSchemasError',
    'FDWOptionNameNotFoundError',
    'FDWOutOfMemoryError',
    'FDWReplyHandleError',
    'FDWSchemaNotFoundError',
    'FDWTableNotFoundError',
    'FDWTooManyHandlesError',
    'FDWUnableToCreateExecutionError',
    'FDWUnableToCreateReplyError',
    'FDWUnableToEstablishConnectionError',
    'FeatureNotSupportedError',
    'FileNameTooLongError',
    'ForeignKeyViolationError',
    'FunctionExecutedNoReturnStatementError',
    'GeneratedAlwaysError',
    'GroupingError',
    'HeldCursorRequiresSameIsolationLevelError',
    'IdleInTransactionSessionTimeoutError',
    'IdleSessionTimeoutError',
    'ImplicitZeroBitPadding',
    'InFailedSQLTransactionError',
    'InappropriateAccessModeForBranchTransactionError',
    'InappropriateIsolationLevelForBranchTransactionError',  # noqa: PYI053
    'IndeterminateCollationError',
    'IndeterminateDatatypeError',
    'IndexCorruptedError',
    'IndicatorOverflowError',
    'InsufficientPrivilegeError',
    'InsufficientResourcesError',
    'IntegrityConstraintViolationError',
    'InternalServerError',
    'IntervalFieldOverflowError',
    'InvalidArgumentForLogarithmError',
    'InvalidArgumentForNthValueFunctionError',
    'InvalidArgumentForNtileFunctionError',
    'InvalidArgumentForPowerFunctionError',
    'InvalidArgumentForSQLJsonDatetimeFunctionError',
    'InvalidArgumentForWidthBucketFunctionError',
    'InvalidArgumentForXqueryError',
    'InvalidAuthorizationSpecificationError',
    'InvalidBinaryRepresentationError',
    'InvalidCachedStatementError',
    'InvalidCatalogNameError',
    'InvalidCharacterValueForCastError',
    'InvalidColumnDefinitionError',
    'InvalidColumnReferenceError',
    'InvalidCursorDefinitionError',
    'InvalidCursorNameError',
    'InvalidCursorStateError',
    'InvalidDatabaseDefinitionError',
    'InvalidDatetimeFormatError',
    'InvalidEscapeCharacterError',
    'InvalidEscapeOctetError',
    'InvalidEscapeSequenceError',
    'InvalidForeignKeyError',
    'InvalidFunctionDefinitionError',
    'InvalidGrantOperationError',
    'InvalidGrantorError',
    'InvalidIndicatorParameterValueError',
    'InvalidJsonTextError',
    'InvalidLocatorSpecificationError',
    'InvalidNameError',
    'InvalidObjectDefinitionError',
    'InvalidParameterValueError',
    'InvalidPasswordError',
    'InvalidPrecedingOrFollowingSizeError',
    'InvalidPreparedStatementDefinitionError',
    'InvalidRecursionError',
    'InvalidRegularExpressionError',
    'InvalidRoleSpecificationError',
    'InvalidRowCountInLimitClauseError',
    'InvalidRowCountInResultOffsetClauseError',
    'InvalidSQLJsonSubscriptError',
    'InvalidSQLStatementNameError',
    'InvalidSavepointSpecificationError',
    'InvalidSchemaDefinitionError',
    'InvalidSchemaNameError',
    'InvalidSqlstateReturnedError',
    'InvalidTableDefinitionError',
    'InvalidTablesampleArgumentError',
    'InvalidTablesampleRepeatError',
    'InvalidTextRepresentationError',
    'InvalidTimeZoneDisplacementValueError',
    'InvalidTransactionInitiationError',
    'InvalidTransactionStateError',
    'InvalidTransactionTerminationError',
    'InvalidUseOfEscapeCharacterError',
    'InvalidXmlCommentError',
    'InvalidXmlContentError',
    'InvalidXmlDocumentError',
    'InvalidXmlProcessingInstructionError',
    'LocatorError',
    'LockFileExistsError',
    'LockNotAvailableError',
    'ModifyingExternalRoutineSQLDataNotPermittedError',
    'ModifyingSQLDataNotPermittedError',
    'MoreThanOneSQLJsonItemError',
    'MostSpecificTypeMismatchError',
    'NameTooLongError',
    'NoActiveSQLTransactionError',
    'NoActiveSQLTransactionForBranchTransactionError',
    'NoAdditionalDynamicResultSetsReturned',
    'NoData',
    'NoDataFoundError',
    'NoSQLJsonItemError',
    'NonNumericSQLJsonItemError',
    'NonUniqueKeysInAJsonObjectError',
    'NonstandardUseOfEscapeCharacterError',
    'NotAnXmlDocumentError',
    'NotNullViolationError',
    'NullValueEliminatedInSetFunction',
    'NullValueInExternalRoutineNotAllowedError',
    'NullValueNoIndicatorParameterError',
    'NullValueNotAllowedError',
    'NumericValueOutOfRangeError',
    'ObjectInUseError',
    'ObjectNotInPrerequisiteStateError',
    'OperatorInterventionError',
    'OutOfMemoryError',
    'PLPGSQLError',
    'PostgresConnectionError',
    'PostgresFloatingPointError',
    'PostgresIOError',
    'PostgresSyntaxError',
    'PostgresSystemError',
    'PostgresWarning',
    'PrivilegeNotGranted',
    'PrivilegeNotRevoked',
    'ProgramLimitExceededError',
    'ProhibitedExternalRoutineSQLStatementAttemptedError',  # noqa: PYI053
    'ProhibitedSQLStatementAttemptedError',
    'ProtocolViolationError',
    'QueryCanceledError',
    'RaiseError',
    'ReadOnlySQLTransactionError',
    'ReadingExternalRoutineSQLDataNotPermittedError',
    'ReadingSQLDataNotPermittedError',
    'ReservedNameError',
    'RestrictViolationError',
    'SQLJsonArrayNotFoundError',
    'SQLJsonItemCannotBeCastToTargetTypeError',
    'SQLJsonMemberNotFoundError',
    'SQLJsonNumberNotFoundError',
    'SQLJsonObjectNotFoundError',
    'SQLJsonScalarRequiredError',
    'SQLRoutineError',
    'SQLStatementNotYetCompleteError',
    'SavepointError',
    'SchemaAndDataStatementMixingNotSupportedError',
    'SequenceGeneratorLimitExceededError',
    'SerializationError',
    'SingletonSQLJsonItemRequiredError',
    'SnapshotTooOldError',
    'SrfProtocolViolatedError',
    'StackedDiagnosticsAccessedWithoutActiveHandlerError',  # noqa: PYI053
    'StatementCompletionUnknownError',
    'StatementTooComplexError',
    'StringDataLengthMismatchError',
    'StringDataRightTruncation',
    'StringDataRightTruncationError',
    'SubstringError',
    'SyntaxOrAccessError',
    'TooManyArgumentsError',
    'TooManyColumnsError',
    'TooManyConnectionsError',
    'TooManyJsonArrayElementsError',
    'TooManyJsonObjectMembersError',
    'TooManyRowsError',
    'TransactionIntegrityConstraintViolationError',
    'TransactionResolutionUnknownError',
    'TransactionRollbackError',
    'TransactionTimeoutError',
    'TriggerProtocolViolatedError',
    'TriggeredActionError',
    'TriggeredDataChangeViolationError',
    'TrimError',
    'UndefinedColumnError',
    'UndefinedFileError',
    'UndefinedFunctionError',
    'UndefinedObjectError',
    'UndefinedParameterError',
    'UndefinedTableError',
    'UniqueViolationError',
    'UnsafeNewEnumValueUsageError',
    'UnterminatedCStringError',
    'UntranslatableCharacterError',
    'WindowingError',
    'WithCheckOptionViolationError',
    'WrongObjectTypeError',
    'ZeroLengthCharacterStringError',
)
