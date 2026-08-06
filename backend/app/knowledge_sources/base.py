from abc import ABC, abstractmethod

class KnowledgeSourceConnector(ABC):
    """Abstract base class for knowledge sources."""

    @abstractmethod
    def connect(self) -> None:
        """Establish a connection to the knowledge source."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Close the connection to the knowledge source."""
        pass

    @abstractmethod
    def start(self) -> None:
        """Start the knowledge source."""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Stop the knowledge source."""
        pass

    @abstractmethod
    def discover_domain(self) -> list:
        """Discover the domain of the knowledge source."""
        pass