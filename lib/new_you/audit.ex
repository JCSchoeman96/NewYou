defmodule NewYou.Audit do
  use Ash.Domain, otp_app: :new_you

  resources do
    resource NewYou.Audit.EvidenceObligation do
      define :establish_registration_obligation, action: :establish_registration
      define :get_evidence_obligation, action: :read, get_by: [:id]

      define :get_registration_obligation_by_source,
        action: :read,
        get_by: [:source_operation_id]

      define :fulfill_evidence_obligation, action: :fulfill
      define :list_evidence_obligations, action: :read
    end

    resource NewYou.Audit.EvidenceRecord do
      define :create_evidence_record, action: :materialize

      define :get_evidence_record_by_obligation,
        action: :read,
        get_by: [:obligation_id],
        not_found_error?: false

      define :list_evidence_records, action: :read
    end
  end
end
