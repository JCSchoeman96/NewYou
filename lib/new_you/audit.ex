defmodule NewYou.Audit do
  use Ash.Domain, otp_app: :new_you

  resources do
    resource NewYou.Audit.EvidenceObligation do
      define :establish_registration_obligation, action: :establish_registration
      define :get_evidence_obligation, action: :read, get_by: [:id]

      define :materialize_registration_evidence, action: :materialize_registration_evidence
    end

    resource NewYou.Audit.EvidenceRecord do
      define :get_evidence_record_by_obligation,
        action: :read,
        get_by: [:obligation_id],
        not_found_error?: false
    end
  end
end
