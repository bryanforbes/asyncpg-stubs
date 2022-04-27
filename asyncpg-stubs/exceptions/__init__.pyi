import typing

from . import _base
from ._base import *

class PostgresWarning(_base.PostgresLogMessage, Warning):
    sqlstate: typing.ClassVar[str]

class DynamicResultSetsReturned(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class ImplicitZeroBitPadding(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class NullValueEliminatedInSetFunction(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class PrivilegeNotGranted(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class PrivilegeNotRevoked(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class StringDataRightTruncation(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class DeprecatedFeature(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class NoData(PostgresWarning):
    sqlstate: typing.ClassVar[str]

class NoAdditionalDynamicResultSetsReturned(NoData):
    sqlstate: typing.ClassVar[str]

class SQLStatementNotYetCompleteError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class PostgresConnectionError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class ConnectionDoesNotExistError(PostgresConnectionError):
    sqlstate: typing.ClassVar[str]

class ConnectionFailureError(PostgresConnectionError):
    sqlstate: typing.ClassVar[str]

class ClientCannotConnectError(PostgresConnectionError):
    sqlstate: typing.ClassVar[str]

class ConnectionRejectionError(PostgresConnectionError):
    sqlstate: typing.ClassVar[str]

class TransactionResolutionUnknownError(PostgresConnectionError):
    sqlstate: typing.ClassVar[str]

class ProtocolViolationError(PostgresConnectionError):
    sqlstate: typing.ClassVar[str]

class TriggeredActionError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class FeatureNotSupportedError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidCachedStatementError(FeatureNotSupportedError): ...

class InvalidTransactionInitiationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class LocatorError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidLocatorSpecificationError(LocatorError):
    sqlstate: typing.ClassVar[str]

class InvalidGrantorError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidGrantOperationError(InvalidGrantorError):
    sqlstate: typing.ClassVar[str]

class InvalidRoleSpecificationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class DiagnosticsError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class StackedDiagnosticsAccessedWithoutActiveHandlerError(DiagnosticsError):
    sqlstate: typing.ClassVar[str]

class CaseNotFoundError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class CardinalityViolationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class DataError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class ArraySubscriptError(DataError):
    sqlstate: typing.ClassVar[str]

class CharacterNotInRepertoireError(DataError):
    sqlstate: typing.ClassVar[str]

class DatetimeFieldOverflowError(DataError):
    sqlstate: typing.ClassVar[str]

class DivisionByZeroError(DataError):
    sqlstate: typing.ClassVar[str]

class ErrorInAssignmentError(DataError):
    sqlstate: typing.ClassVar[str]

class EscapeCharacterConflictError(DataError):
    sqlstate: typing.ClassVar[str]

class IndicatorOverflowError(DataError):
    sqlstate: typing.ClassVar[str]

class IntervalFieldOverflowError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidArgumentForLogarithmError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidArgumentForNtileFunctionError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidArgumentForNthValueFunctionError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidArgumentForPowerFunctionError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidArgumentForWidthBucketFunctionError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidCharacterValueForCastError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidDatetimeFormatError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidEscapeCharacterError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidEscapeOctetError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidEscapeSequenceError(DataError):
    sqlstate: typing.ClassVar[str]

class NonstandardUseOfEscapeCharacterError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidIndicatorParameterValueError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidParameterValueError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidPrecedingOrFollowingSizeError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidRegularExpressionError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidRowCountInLimitClauseError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidRowCountInResultOffsetClauseError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidTablesampleArgumentError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidTablesampleRepeatError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidTimeZoneDisplacementValueError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidUseOfEscapeCharacterError(DataError):
    sqlstate: typing.ClassVar[str]

class MostSpecificTypeMismatchError(DataError):
    sqlstate: typing.ClassVar[str]

class NullValueNotAllowedError(DataError):
    sqlstate: typing.ClassVar[str]

class NullValueNoIndicatorParameterError(DataError):
    sqlstate: typing.ClassVar[str]

class NumericValueOutOfRangeError(DataError):
    sqlstate: typing.ClassVar[str]

class SequenceGeneratorLimitExceededError(DataError):
    sqlstate: typing.ClassVar[str]

class StringDataLengthMismatchError(DataError):
    sqlstate: typing.ClassVar[str]

class StringDataRightTruncationError(DataError):
    sqlstate: typing.ClassVar[str]

class SubstringError(DataError):
    sqlstate: typing.ClassVar[str]

class TrimError(DataError):
    sqlstate: typing.ClassVar[str]

class UnterminatedCStringError(DataError):
    sqlstate: typing.ClassVar[str]

class ZeroLengthCharacterStringError(DataError):
    sqlstate: typing.ClassVar[str]

class PostgresFloatingPointError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidTextRepresentationError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidBinaryRepresentationError(DataError):
    sqlstate: typing.ClassVar[str]

class BadCopyFileFormatError(DataError):
    sqlstate: typing.ClassVar[str]

class UntranslatableCharacterError(DataError):
    sqlstate: typing.ClassVar[str]

class NotAnXmlDocumentError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidXmlDocumentError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidXmlContentError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidXmlCommentError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidXmlProcessingInstructionError(DataError):
    sqlstate: typing.ClassVar[str]

class DuplicateJsonObjectKeyValueError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidArgumentForSQLJsonDatetimeFunctionError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidJsonTextError(DataError):
    sqlstate: typing.ClassVar[str]

class InvalidSQLJsonSubscriptError(DataError):
    sqlstate: typing.ClassVar[str]

class MoreThanOneSQLJsonItemError(DataError):
    sqlstate: typing.ClassVar[str]

class NoSQLJsonItemError(DataError):
    sqlstate: typing.ClassVar[str]

class NonNumericSQLJsonItemError(DataError):
    sqlstate: typing.ClassVar[str]

class NonUniqueKeysInAJsonObjectError(DataError):
    sqlstate: typing.ClassVar[str]

class SingletonSQLJsonItemRequiredError(DataError):
    sqlstate: typing.ClassVar[str]

class SQLJsonArrayNotFoundError(DataError):
    sqlstate: typing.ClassVar[str]

class SQLJsonMemberNotFoundError(DataError):
    sqlstate: typing.ClassVar[str]

class SQLJsonNumberNotFoundError(DataError):
    sqlstate: typing.ClassVar[str]

class SQLJsonObjectNotFoundError(DataError):
    sqlstate: typing.ClassVar[str]

class TooManyJsonArrayElementsError(DataError):
    sqlstate: typing.ClassVar[str]

class TooManyJsonObjectMembersError(DataError):
    sqlstate: typing.ClassVar[str]

class SQLJsonScalarRequiredError(DataError):
    sqlstate: typing.ClassVar[str]

class IntegrityConstraintViolationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class RestrictViolationError(IntegrityConstraintViolationError):
    sqlstate: typing.ClassVar[str]

class NotNullViolationError(IntegrityConstraintViolationError):
    sqlstate: typing.ClassVar[str]

class ForeignKeyViolationError(IntegrityConstraintViolationError):
    sqlstate: typing.ClassVar[str]

class UniqueViolationError(IntegrityConstraintViolationError):
    sqlstate: typing.ClassVar[str]

class CheckViolationError(IntegrityConstraintViolationError):
    sqlstate: typing.ClassVar[str]

class ExclusionViolationError(IntegrityConstraintViolationError):
    sqlstate: typing.ClassVar[str]

class InvalidCursorStateError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidTransactionStateError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class ActiveSQLTransactionError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class BranchTransactionAlreadyActiveError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class HeldCursorRequiresSameIsolationLevelError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class InappropriateAccessModeForBranchTransactionError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class InappropriateIsolationLevelForBranchTransactionError(
    InvalidTransactionStateError
):
    sqlstate: typing.ClassVar[str]

class NoActiveSQLTransactionForBranchTransactionError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class ReadOnlySQLTransactionError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class SchemaAndDataStatementMixingNotSupportedError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class NoActiveSQLTransactionError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class InFailedSQLTransactionError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class IdleInTransactionSessionTimeoutError(InvalidTransactionStateError):
    sqlstate: typing.ClassVar[str]

class InvalidSQLStatementNameError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class TriggeredDataChangeViolationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidAuthorizationSpecificationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidPasswordError(InvalidAuthorizationSpecificationError):
    sqlstate: typing.ClassVar[str]

class DependentPrivilegeDescriptorsStillExistError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class DependentObjectsStillExistError(DependentPrivilegeDescriptorsStillExistError):
    sqlstate: typing.ClassVar[str]

class InvalidTransactionTerminationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class SQLRoutineError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class FunctionExecutedNoReturnStatementError(SQLRoutineError):
    sqlstate: typing.ClassVar[str]

class ModifyingSQLDataNotPermittedError(SQLRoutineError):
    sqlstate: typing.ClassVar[str]

class ProhibitedSQLStatementAttemptedError(SQLRoutineError):
    sqlstate: typing.ClassVar[str]

class ReadingSQLDataNotPermittedError(SQLRoutineError):
    sqlstate: typing.ClassVar[str]

class InvalidCursorNameError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class ExternalRoutineError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class ContainingSQLNotPermittedError(ExternalRoutineError):
    sqlstate: typing.ClassVar[str]

class ModifyingExternalRoutineSQLDataNotPermittedError(ExternalRoutineError):
    sqlstate: typing.ClassVar[str]

class ProhibitedExternalRoutineSQLStatementAttemptedError(ExternalRoutineError):
    sqlstate: typing.ClassVar[str]

class ReadingExternalRoutineSQLDataNotPermittedError(ExternalRoutineError):
    sqlstate: typing.ClassVar[str]

class ExternalRoutineInvocationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidSqlstateReturnedError(ExternalRoutineInvocationError):
    sqlstate: typing.ClassVar[str]

class NullValueInExternalRoutineNotAllowedError(ExternalRoutineInvocationError):
    sqlstate: typing.ClassVar[str]

class TriggerProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: typing.ClassVar[str]

class SrfProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: typing.ClassVar[str]

class EventTriggerProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: typing.ClassVar[str]

class SavepointError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidSavepointSpecificationError(SavepointError):
    sqlstate: typing.ClassVar[str]

class InvalidCatalogNameError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InvalidSchemaNameError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class TransactionRollbackError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class TransactionIntegrityConstraintViolationError(TransactionRollbackError):
    sqlstate: typing.ClassVar[str]

class SerializationError(TransactionRollbackError):
    sqlstate: typing.ClassVar[str]

class StatementCompletionUnknownError(TransactionRollbackError):
    sqlstate: typing.ClassVar[str]

class DeadlockDetectedError(TransactionRollbackError):
    sqlstate: typing.ClassVar[str]

class SyntaxOrAccessError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class PostgresSyntaxError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InsufficientPrivilegeError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class CannotCoerceError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class GroupingError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class WindowingError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidRecursionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidForeignKeyError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidNameError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class NameTooLongError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class ReservedNameError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DatatypeMismatchError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class IndeterminateDatatypeError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class CollationMismatchError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class IndeterminateCollationError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class WrongObjectTypeError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class GeneratedAlwaysError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class UndefinedColumnError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class UndefinedFunctionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class UndefinedTableError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class UndefinedParameterError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class UndefinedObjectError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateColumnError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateCursorError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateDatabaseError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateFunctionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicatePreparedStatementError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateSchemaError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateTableError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateAliasError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class DuplicateObjectError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class AmbiguousColumnError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class AmbiguousFunctionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class AmbiguousParameterError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class AmbiguousAliasError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidColumnReferenceError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidColumnDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidCursorDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidDatabaseDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidFunctionDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidPreparedStatementDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidSchemaDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidTableDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class InvalidObjectDefinitionError(SyntaxOrAccessError):
    sqlstate: typing.ClassVar[str]

class WithCheckOptionViolationError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class InsufficientResourcesError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class DiskFullError(InsufficientResourcesError):
    sqlstate: typing.ClassVar[str]

class OutOfMemoryError(InsufficientResourcesError):
    sqlstate: typing.ClassVar[str]

class TooManyConnectionsError(InsufficientResourcesError):
    sqlstate: typing.ClassVar[str]

class ConfigurationLimitExceededError(InsufficientResourcesError):
    sqlstate: typing.ClassVar[str]

class ProgramLimitExceededError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class StatementTooComplexError(ProgramLimitExceededError):
    sqlstate: typing.ClassVar[str]

class TooManyColumnsError(ProgramLimitExceededError):
    sqlstate: typing.ClassVar[str]

class TooManyArgumentsError(ProgramLimitExceededError):
    sqlstate: typing.ClassVar[str]

class ObjectNotInPrerequisiteStateError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class ObjectInUseError(ObjectNotInPrerequisiteStateError):
    sqlstate: typing.ClassVar[str]

class CantChangeRuntimeParamError(ObjectNotInPrerequisiteStateError):
    sqlstate: typing.ClassVar[str]

class LockNotAvailableError(ObjectNotInPrerequisiteStateError):
    sqlstate: typing.ClassVar[str]

class UnsafeNewEnumValueUsageError(ObjectNotInPrerequisiteStateError):
    sqlstate: typing.ClassVar[str]

class OperatorInterventionError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class QueryCanceledError(OperatorInterventionError):
    sqlstate: typing.ClassVar[str]

class AdminShutdownError(OperatorInterventionError):
    sqlstate: typing.ClassVar[str]

class CrashShutdownError(OperatorInterventionError):
    sqlstate: typing.ClassVar[str]

class CannotConnectNowError(OperatorInterventionError):
    sqlstate: typing.ClassVar[str]

class DatabaseDroppedError(OperatorInterventionError):
    sqlstate: typing.ClassVar[str]

class IdleSessionTimeoutError(OperatorInterventionError):
    sqlstate: typing.ClassVar[str]

class PostgresSystemError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class PostgresIOError(PostgresSystemError):
    sqlstate: typing.ClassVar[str]

class UndefinedFileError(PostgresSystemError):
    sqlstate: typing.ClassVar[str]

class DuplicateFileError(PostgresSystemError):
    sqlstate: typing.ClassVar[str]

class SnapshotTooOldError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class ConfigFileError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class LockFileExistsError(ConfigFileError):
    sqlstate: typing.ClassVar[str]

class FDWError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class FDWColumnNameNotFoundError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWDynamicParameterValueNeededError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWFunctionSequenceError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInconsistentDescriptorInformationError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidAttributeValueError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidColumnNameError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidColumnNumberError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidDataTypeError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidDataTypeDescriptorsError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidDescriptorFieldIdentifierError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidHandleError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidOptionIndexError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidOptionNameError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidStringLengthOrBufferLengthError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidStringFormatError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWInvalidUseOfNullPointerError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWTooManyHandlesError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWOutOfMemoryError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWNoSchemasError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWOptionNameNotFoundError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWReplyHandleError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWSchemaNotFoundError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWTableNotFoundError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWUnableToCreateExecutionError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWUnableToCreateReplyError(FDWError):
    sqlstate: typing.ClassVar[str]

class FDWUnableToEstablishConnectionError(FDWError):
    sqlstate: typing.ClassVar[str]

class PLPGSQLError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class RaiseError(PLPGSQLError):
    sqlstate: typing.ClassVar[str]

class NoDataFoundError(PLPGSQLError):
    sqlstate: typing.ClassVar[str]

class TooManyRowsError(PLPGSQLError):
    sqlstate: typing.ClassVar[str]

class AssertError(PLPGSQLError):
    sqlstate: typing.ClassVar[str]

class InternalServerError(_base.PostgresError):
    sqlstate: typing.ClassVar[str]

class DataCorruptedError(InternalServerError):
    sqlstate: typing.ClassVar[str]

class IndexCorruptedError(InternalServerError):
    sqlstate: typing.ClassVar[str]

__all__ = [
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
    'InappropriateIsolationLevelForBranchTransactionError',
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
    'ProhibitedExternalRoutineSQLStatementAttemptedError',
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
    'StackedDiagnosticsAccessedWithoutActiveHandlerError',
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
]
__all__ += _base.__all__
